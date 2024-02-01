package com.example.springApi.demo.entity

import jakarta.persistence.CascadeType
import jakarta.persistence.Column
import jakarta.persistence.Embedded
import jakarta.persistence.Entity
import jakarta.persistence.FetchType
import jakarta.persistence.GeneratedValue
import jakarta.persistence.GenerationType
import jakarta.persistence.Id
import jakarta.persistence.OneToMany
import jakarta.persistence.Table

@Entity
@Table(name = "Cliente")
data class Customer(
    @Column(nullable = false) var fistName: String = "",
    @Column(nullable = false) var lastName: String = "",
    @Column(nullable = false, unique = true) val cpf: String = "",
    @Column(nullable = false, unique = true) var email: String = "",
    @Column(nullable = false) var password: String = "",
    @Column(nullable = false)  @Embedded var address: Address = Address(),
    @Column(nullable = false) @OneToMany(fetch = FetchType.LAZY, cascade = [CascadeType.REMOVE, CascadeType.PERSIST], mappedBy = "customer")
    var credits: List<Credit> = mutableListOf(),
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY) val id:Long?=   null //primary key for the table with this annotation.

    )
