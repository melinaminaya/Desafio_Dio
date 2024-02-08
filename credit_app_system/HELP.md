# Getting Started

### Reference Documentation
For further reference, please consider the following sections:

* [Official Gradle documentation](https://docs.gradle.org)
* [Spring Boot Gradle Plugin Reference Guide](https://docs.spring.io/spring-boot/docs/3.2.2/gradle-plugin/reference/html/)
* [Create an OCI image](https://docs.spring.io/spring-boot/docs/3.2.2/gradle-plugin/reference/html/#build-image)
* [Spring Web](https://docs.spring.io/spring-boot/docs/3.2.2/reference/htmlsingle/index.html#web)
* [Validation](https://docs.spring.io/spring-boot/docs/3.2.2/reference/htmlsingle/index.html#io.validation)
* [Spring Data JPA](https://docs.spring.io/spring-boot/docs/3.2.2/reference/htmlsingle/index.html#data.sql.jpa-and-spring-data)
* [Flyway Migration](https://docs.spring.io/spring-boot/docs/3.2.2/reference/htmlsingle/index.html#howto.data-initialization.migration-tool.flyway)

### Guides
The following guides illustrate how to use some features concretely:

* [Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/)
* [Serving Web Content with Spring MVC](https://spring.io/guides/gs/serving-web-content/)
* [Building REST services with Spring](https://spring.io/guides/tutorials/rest/)
* [Validation](https://spring.io/guides/gs/validating-form-input/)
* [Accessing Data with JPA](https://spring.io/guides/gs/accessing-data-jpa/)

### Additional Links
These additional references should also help you:

* [Gradle Build Scans – insights for your project's build](https://scans.gradle.com#gradle)
* [Common docs reference for application.yml](https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#appendix.application-properties)
* [All JPA annotations](https://strn.com.br/artigos/2018/12/11/todas-as-anota%C3%A7%C3%B5es-do-jpa-anota%C3%A7%C3%B5es-de-mapeamento/)

### Structure
Composed by 3 layers: Model, Service and Controller.
1. Controller: all DTOs (data transfer objects) and endpoints.
2. Model: dataclasses by Entities.
3. Service: register data in DB.

### ApiEndpoints
Requests Customer or Credit Info:
#### Customer
    1. POST Include Customer
        a. Request: firstName, lastName, cpf, income, email, password,  zipCode and Street.
        b. Response: String
    2. PUT Update Customer
        a. Request: id, firstName, lastName, income, zipCode, street.
        b. Response: firstName, lastName, income, cpf, email, income, zipCode, street.
    3. GET Customer
        a. Request: id
        b. Response: firstName, lastName, income,cpf, email, income, zipCode, street.
    4. POST Delete Customer
        a. Request: id
        b. Response: ""
#### Credit
    1. POST Include Credit(Loan)
        a. Request: creditValue, dayFirstOfInstallment, numberOfInstallments and customerId.
        b. Response: String
    2. GET ListAllCustomerLoans
        a. Request: customerId
        b. Response: creditCode, creditValue, numberOfInstallment.
    3. GET Loan
        a. Request: customerId, creditCode
        b. Response: creditCode, creditValue, numberOfInstallment, status, emailCustomer and incomeCustomer.