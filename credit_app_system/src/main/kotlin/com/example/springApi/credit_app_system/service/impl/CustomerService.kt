package com.example.springApi.credit_app_system.service.impl

import com.example.springApi.credit_app_system.entity.Customer
import com.example.springApi.credit_app_system.exceptions.BusinessException
import com.example.springApi.credit_app_system.repository.CustomerRepository
import com.example.springApi.credit_app_system.service.ICustomerService
import org.springframework.stereotype.Service

@Service //obligatory annnotation
class CustomerService(private val customerRepository: CustomerRepository) : ICustomerService {

    override fun save(customer: Customer): Customer =
        this.customerRepository.save(customer)


    override fun findById(id: Long): Customer =
        this.customerRepository.findById(id).orElseThrow {
            throw BusinessException("ID $id not found")
        }

    override fun delete(id: Long) {
       val customer:Customer = this.findById(id)
       this.customerRepository.delete(customer)
    }
}