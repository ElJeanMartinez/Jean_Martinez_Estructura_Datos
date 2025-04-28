package com.mycompany.proyectoestructura;

import java.util.Stack;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Jean Martinez
 */
public class listaclientes {
    private nodo cabeza;

    public listaclientes() {
        cabeza = null;
    }

    // Insertar ordenado por cédula
    public void insertarOrdenado(cliente Cliente) {
        nodo nuevo = new nodo(Cliente);
        if (cabeza == null || Cliente.getCedula() < cabeza.cliente.getCedula()) {
            nuevo.siguiente = cabeza;
            cabeza = nuevo;
        } else {
            nodo actual = cabeza;
            while (actual.siguiente != null &&
                   Cliente.getCedula() > actual.siguiente.cliente.getCedula()) {
                actual = actual.siguiente;
            }
            nuevo.siguiente = actual.siguiente;
            actual.siguiente = nuevo;
        }
    }

    public nodo getCabeza() {
        return cabeza;
    }

    // Método para listar la lista en orden inverso
    public String listarInverso() {
        nodo actual = cabeza;
        StringBuilder listaInversa = new StringBuilder();

        if (actual == null) {
            listaInversa.append("Lista vacía.");
        } else {
            // Usamos una pila para invertir el orden de la lista
            Stack<cliente> pila = new Stack<>();
            while (actual != null) {
                pila.push(actual.cliente);
                actual = actual.siguiente;
            }

            // Ahora mostramos la lista invertida
            while (!pila.isEmpty()) {
                listaInversa.append(pila.pop()).append("\n");
            }
        }

        return listaInversa.toString(); // Retornamos la lista invertida como un String
    }
}


