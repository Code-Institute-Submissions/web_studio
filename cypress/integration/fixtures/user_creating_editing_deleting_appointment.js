Cypress.Cookies.defaults({
    preserve: "csrftoken"
})

describe('User creating, editing, deleting appointment', () => {


    it(
        'it will create appointment',
        () => {


            cy.visit('http://127.0.0.1:8000/consultations')
                .then(() => {
                    cy.get('[data-cy=name]')
                        .should('be.visible')
                        .type('Test Customer')
                        .should('have.value', 'Test Customer');
                    cy.get('[data-cy=email]')
                        .should('be.visible')
                        .type('cypress@email.com')
                        .should('have.value', 'cypress@email.com');
                    cy.get('[data-cy=phone_num]')
                        .should('be.visible')
                        .type('0876707891')
                        .should('have.value', '0876707891');
                    cy.get('[data-cy=password]')
                        .should('be.visible')
                        .type('password')
                        .should('have.value', 'password');
                    cy.get('[data-cy=time_slot]')
                        .should('be.visible')
                        .select('8 am - 12 am');
                    cy.get('[data-cy=site_type]')
                        .should('be.visible')
                        .select('blog');

                    cy.get('[data-cy=project]')
                        .should('be.visible')
                        .type('This is the biggest project yet!')
                        .should('have.value', 'This is the biggest project yet!');

                    cy.get('[data-cy=submit]')
                        .should('be.visible')
                        .click();

                    cy.wait(1000);


                });


        }
    );

    it(
        'it will sign in newly created user',
        () => {


            cy.get('#id_login')
                .should('be.visible')
                .type('cypress@email.com')
                .should('have.value', 'cypress@email.com');
            cy.get('#id_password')
                .should('be.visible')
                .type('password')
                .should('have.value', 'password');


            cy.get('[data-cy=sign_in]')
                .should('be.visible')
                .click();

            cy.wait(1000);


        }
    );


    it(
        'it will edit appointment',
        () => {
            cy.get('[data-cy=edit_consultation]')
                .should('be.visible')
                .click();


            cy.get('[data-cy=site_type]')

                .should('be.visible')
                .select('website');

            cy.get('[data-cy=project]')
                .should('be.visible')
                .clear()
                .type('This is different project!')
                .should('have.value', 'This is different project!');

            cy.get('[data-cy=update_appointment]')
                .should('be.visible')
                .click();

            cy.wait(4000);


        }
    );
    it(
        'it will sign in and  check newly edited appointment and delete it',
        () => {


            cy.get('#id_login')
                .should('be.visible')
                .type('cypress@email.com')
                .should('have.value', 'cypress@email.com');
            cy.get('#id_password')
                .should('be.visible')
                .type('password')
                .should('have.value', 'password');


            cy.get('[data-cy=sign_in]')
                .should('be.visible')
                .click();

            cy.wait(4000);

            cy.get('[data-cy=edit_consultation]')
                .should('be.visible')
                .click();

            cy.wait(4000);


            cy.get('[data-cy=site_type]')

                .select('website');

            cy.get('[data-cy=project]').scrollIntoView()
                .should('be.visible')

                .should('have.value', 'This is different project!');
            cy.wait(4000);
            cy.get('[data-cy=delete_appointment]').scrollIntoView()
                .should('be.visible')
                .click();

            cy.wait(1000);


        }
    );


});