package com.example.springApi.credit_app_system.dto

import com.example.springApi.credit_app_system.entity.Address
import com.example.springApi.credit_app_system.entity.Customer
import java.math.BigDecimal

data class CustomerUpdateDto(
    val firstName: String,
    val lastName: String,
    val income: BigDecimal,
    val zipCode: String,
    val rua: String
){
    fun toEntity(customer: Customer): Customer {
        customer.firstName = this.firstName
        customer.lastName = this.lastName
        customer.income = this.income
        customer.address.zipCode = this.zipCode
        customer.address.rua = this.rua
        return customer

    }
}
