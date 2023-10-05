from selene import browser, have, be, by
import os

def test_form_demoqa():

    browser.open('/automation-practice-form')

    browser.should(have.title('DEMOQA'))
    browser.element('.main-header').should(have.text('Practice Form'))

    browser.element('#firstName').type('Test_Name')
    browser.element('#lastName').type('Test_Last_Name')
    browser.element('#userEmail').type('test@gmail.com')
    browser.all('.custom-control-input').should(be.disabled)
    browser.element('#gender-radio-1').double_click()
    browser.element('#gender-radio-1').should(be.enabled)
    browser.element('#userNumber').type('8800555353')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('December')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2000')).click()
    browser.element('.react-datepicker__day--011').click()
    browser.element('#subjectsInput').should(be.blank).type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/kotenok-morda-lapyi-hvost.jpg'))
    browser.element('#currentAddress').type('Test_Adress, 9')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('tr td:nth-child(2)').should(have.texts(
        'Test_Name Test_Last_Name',
        'test@gmail.com',
        'Male',
        '8800555353',
        '11 December,2000',
        'Computer Science',
        'Sports',
        'kotenok-morda-lapyi-hvost.jpg',
        'Test_Adress, 9',
        'NCR Delhi'))
    browser.element('#closeLargeModal').press_enter()
