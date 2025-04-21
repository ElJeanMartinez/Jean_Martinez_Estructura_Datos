package com.mycompany.proyectoestructura;

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
        if (cabeza == null || Cliente.getCedula().compareTo(cabeza.cliente.getCedula()) < 0) {
            nuevo.siguiente = cabeza;
            cabeza = nuevo;
        } else {
            nodo actual = cabeza;
            while (actual.siguiente != null &&
                   Cliente.getCedula().compareTo(actual.siguiente.cliente.getCedula()) > 0) {
                actual = actual.siguiente;
            }
            nuevo.siguiente = actual.siguiente;
            actual.siguiente = nuevo;
        }
    }

    public void listar() {
        nodo actual = cabeza;
        if (actual == null) {
            System.out.println("Lista vacia.");
            return;
        }
        while (actual != null) {
            System.out.println(actual.cliente);
            actual = actual.siguiente;
        }
    }
}


