/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.proyectoestructura;

/**
 *
 * @author Jean Martinez
 */
public class nodo {
    cliente cliente;
    nodo siguiente;

    public nodo(cliente cliente) {
        this.cliente = cliente;
        this.siguiente = null;
    }
}

