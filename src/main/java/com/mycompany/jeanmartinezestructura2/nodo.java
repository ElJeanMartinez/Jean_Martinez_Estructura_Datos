/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.jeanmartinezestructura2;

/**
 *
 * @author Estudiante
 */
//datos
public class nodo {
    cliente cliente;
    nodo siguiente;
    nodo anterior;

    public nodo(cliente cliente) {
        this.cliente = cliente;
        this.siguiente = null;
        this.anterior = null;
    }
}
