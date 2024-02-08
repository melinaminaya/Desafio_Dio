package com.example.springApi.credit_app_system.dto

import com.example.springApi.credit_app_system.entity.Credit
import com.example.springApi.credit_app_system.entity.Customer
import jakarta.validation.constraints.Future
import jakarta.validation.constraints.NotEmpty
import jakarta.validation.constraints.NotNull
import java.math.BigDecimal
import java.time.LocalDate

data class CreditDto(
    @field:NotNull(message = "Invalid input") val creditValue: BigDecimal,
    @field:Future val dayFirstOfInstallment: LocalDate,
    @field:NotNull(message = "Invalid input") val numberOfInstallments: Int,
    @field:NotNull(message = "Invalid input") val customerId: Long
) {
fun toEntity(): Credit =
    Credit(
        creditValue = this.creditValue,
        dayFirstInstallmentval = this.dayFirstOfInstallment,
        numberOfInstallments = this.numberOfInstallments,
        customer = Customer(id = this.customerId)
    )

}
