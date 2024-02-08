package com.example.springApi.credit_app_system.entity

import jakarta.persistence.Embeddable

@Embeddable
data class Address(
var zipCode: String = "",
    var rua : String = "",
)
