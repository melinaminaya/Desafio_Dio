package com.example.springApi.credit_app_system.service

import com.example.springApi.credit_app_system.entity.Customer

interface ICustomerService {
    fun save(customer:Customer):Customer
    fun findById(id: Long):Customer
    fun delete(id: Long)
}