package com.example.springApi.credit_app_system.dto

import com.example.springApi.credit_app_system.entity.Credit
import com.example.springApi.credit_app_system.entity.Customer
import java.math.BigDecimal
import java.time.LocalDate

data class CreditDto(
    val creditValue: BigDecimal,
    val dayFirstOfInstallment: LocalDate,
    val numberOfInstallments: Int,
    val customerId: Long
) {
fun toEntity(): Credit =
    Credit(
        creditValue = this.creditValue,
        dayFirstInstallmentval = this.dayFirstOfInstallment,
        numberOfInstallments = this.numberOfInstallments,
        customer = Customer(id = this.customerId)
    )

}
