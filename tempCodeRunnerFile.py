e_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(@class, 'sc-7352ee5b-1')]")
    )
)
show_more_button.click()