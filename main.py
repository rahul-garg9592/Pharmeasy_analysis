from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://pharmeasy.in/diagnostics/all-tests")
wait = WebDriverWait(driver, 20)

def count_items():
    search_boxes = driver.find_elements(By.CLASS_NAME, "sc-b6bb78f6-0")
    return len(search_boxes)

previous_count = 0

while True:
    current_count = count_items()
    print(f"Items found so far: {current_count}")
    
    if current_count == previous_count:
        print("No new items added. Exiting loop.")
        break
    previous_count = current_count

    try:
        show_more_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Show More')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -150);", show_more_button)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Show More')]")))
        driver.execute_script("arguments[0].click();", show_more_button)
        wait.until(lambda d: count_items() > previous_count)
    except Exception as e:
        print("No more 'Show More' button found or no new items loaded.")
        print("Error:", e)
        break

search_boxes = driver.find_elements(By.CLASS_NAME, "sc-b6bb78f6-0")
print("Total items found:", len(search_boxes))
file = 1
for box in search_boxes:
    d = box.get_attribute("outerHTML")
    with open(f"data/test_{file}.html", "w" ,encoding="utf-8") as f:
        f.write(d)
    file += 1
driver.quit()
