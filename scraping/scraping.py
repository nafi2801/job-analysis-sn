import requests
from bs4 import BeautifulSoup
import json
import csv

def scrape_emploidakar_jobs():
    url = "https://www.emploidakar.com/jm-ajax/get_listings/"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    all_jobs = []
    page = 1
    
    while True:
        print(f"Scraping page {page}...")
        
        payload = {
            'search_keywords': '',
            'search_location': '',
            'filter_job_type[]': ['cdd', 'cdi', 'freelance', 'prestation-de-services', 'stage', ''],
            'per_page': 17,
            'orderby': 'featured',
            'featured_first': 'false',
            'order': 'DESC',
            'page': page,
            'show_pagination': 'true'
        }
        
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code != 200:
            print(f"Failed to get page {page}, status code: {response.status_code}")
            break
        
        data = json.loads(response.text)
        html_content = data.get('html', '')
        soup = BeautifulSoup(html_content, 'html.parser')
        job_cards = soup.find_all('li', class_='job_listing')
        
        if not job_cards:
            print("No more jobs found, ending scraping.")
            break
        
        for job in job_cards:
            title = job.find('h3')
            company = job.find('div', class_='company')
            location = job.find('div', class_='location')
            job_type = job.find('li', class_='job-type')
            date = job.find('li', class_='date')
            
            job_data = {
                'title': title.get_text(strip=True) if title else None,
                'company': company.get_text(strip=True) if company else None,
                'location': location.get_text(strip=True) if location else None,
                'job_type': job_type.get_text(strip=True) if job_type else None,
                'date_posted': date.get_text(strip=True) if date else None,
            }
            
            all_jobs.append(job_data)
        
        page += 1
    
    print(f"Scraped total {len(all_jobs)} jobs.")
    return all_jobs

def save_jobs_to_csv(jobs, filename='jobs.csv'):
    if not jobs:
        print("No jobs to save.")
        return
    
    keys = jobs[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(jobs)
    print(f"Saved {len(jobs)} jobs to {filename}")

if __name__ == "__main__":
    jobs = scrape_emploidakar_jobs()
    if jobs:
        for i, job in enumerate(jobs[:5], 1):
            print(f"Job {i}: {job}")
    save_jobs_to_csv(jobs)
