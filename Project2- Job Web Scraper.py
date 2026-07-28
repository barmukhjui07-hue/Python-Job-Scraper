import urllib.request
print("=== MY FIRST PYTHON JOB SCRAPER ===")
print("Fetching jobs from website...")
url = "https://realpython.github.io/fake-jobs/"
website = urllib.request.urlopen(url)
job_count = 0

for line in website:
    text = line.decode('utf-8')
    if '<h2 class="title is-5">' in text:
        clean_title = text.replace('<h2 class="title is-5">', '').replace('</h2>', '').strip()
        job_count += 1
        print(f"Job #{job_count}: {clean_title}")
        if job_count == 5:
            break
print("Done! All 5 jobs extracted.")
