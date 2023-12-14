from selene import browser, have
import os


def test_form_of_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Bebish')
    browser.element('#lastName').type('Bebushov')
    browser.element('#userEmail').type('beb.bobushov@mail.ru')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9091234567')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click().type('April').click()
    browser.element('[class="react-datepicker__year-select"]').click().type('1994').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--028"]').click()
    browser.element('#subjectsInput').click().type('History').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('[type=file]').send_keys(os.path.abspath('crazyduck.jpg'))
    browser.element('#currentAddress').type('Moscow leskova')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').click()

    # checking

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Bebish Bebushov'))
    browser.element('.modal-body').should(have.text('beb.bobushov@mail.ru'))
    browser.element('.modal-body').should(have.text('Male'))
    browser.element('.modal-body').should(have.text('9091234567'))
    browser.element('.modal-body').should(have.text('28 April,1994'))
    browser.element('.modal-body').should(have.text('history'))
    browser.element('.modal-body').should(have.text('Sports'))
    browser.element('.modal-body').should(have.text('crazyduck.jpg'))
    browser.element('.modal-body').should(have.text('Moscow leskova'))
    browser.element('.modal-body').should(have.text('NCR Noida'))
