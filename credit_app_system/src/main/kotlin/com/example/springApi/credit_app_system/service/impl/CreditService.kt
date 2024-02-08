package com.example.springApi.credit_app_system.service.impl

import com.example.springApi.credit_app_system.entity.Credit
import com.example.springApi.credit_app_system.exceptions.BusinessException
import com.example.springApi.credit_app_system.repository.CreditRepository
import com.example.springApi.credit_app_system.service.ICreditService
import org.springframework.stereotype.Service
import java.lang.IllegalArgumentException
import java.util.UUID

@Service
class CreditService(private val creditRepository: CreditRepository, private val customerService: CustomerService): ICreditService {
    override fun save(credit: Credit): Credit {
        credit.apply {
            customer = customerService.findById(credit.customer?.id!!)
        }
        return this.creditRepository.save(credit)
    }
    override fun findAllByCustomer(customerId: Long): List<Credit> = this.creditRepository.findAllByCredits(customerId)

    /**
     * Compare the customer id with the creditCustomerId.
     * Use NamedQuery in JPA References: docs.spring.io
     */
    override fun findByCreditCode(customerId:Long, creditCode: UUID): Credit {
        val credit = this.creditRepository.findByCreditCode(creditCode)?: throw BusinessException("Credit not found")
        return if(credit.customer?.id == customerId) credit else throw IllegalArgumentException("Contact Admin")
    }
}