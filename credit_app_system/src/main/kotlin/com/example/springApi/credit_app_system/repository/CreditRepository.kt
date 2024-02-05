package com.example.springApi.credit_app_system.repository

import com.example.springApi.credit_app_system.entity.Credit
import org.springframework.data.jpa.repository.JpaRepository
import org.springframework.data.jpa.repository.Query
import org.springframework.stereotype.Repository
import java.util.UUID

/**
 * JPARepository is a CRUD to access DB.
 */
@Repository
interface CreditRepository : JpaRepository<Credit, Long> {
    fun findByCreditCode(creditCode: UUID): Credit

    /**
     * Same query used in BD to make a search.
     * Reference: [Link to Spring Docs](https://docs.spring.io/spring-data/jpa/reference/jpa/query-methods.html#jpa.query-methods.at-query)
     */
    @Query(value = "SELECT * FROM CREDIT WHERE CUSTOMER_ID = ?1", nativeQuery = true)
    fun findAllByCredits(customerId: Long): List<Credit>
}