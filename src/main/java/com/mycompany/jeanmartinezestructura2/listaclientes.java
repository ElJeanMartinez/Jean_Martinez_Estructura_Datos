/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.jeanmartinezestructura2;

/**
 *
 * @author Estudiante
 */
public class listaclientes {
    //referencia al primer registro
    private nodo cabeza;

    //esta vacia
    public listaclientes() {
        cabeza = null;
    }

    
    public void insertarOrdenado(cliente Cliente) {
        nodo nuevo = new nodo(Cliente);

        //si la lista esta vacia el primer registro se pone de primeras
        if (cabeza == null) {
            cabeza = nuevo;
        //se hace la accion de ordenar la lista si la cedula es menor
        } else if (Cliente.getCedula().compareTo(cabeza.cliente.getCedula()) < 0) {
            nuevo.siguiente = cabeza;
            cabeza.anterior = nuevo;
            cabeza = nuevo;
        //recorre la lista hasta saber donde poner el nuevo cliente registrado
        //el nuevo registro compara con los registros de la lista para saber su posicion
        } else {
            nodo actual = cabeza;
            //el nodo se compara si es mayor que la del siguiente nodo, inserta el nodo antes de un nodo mayor o igual
            while (actual.siguiente != null && Cliente.getCedula().compareTo(actual.siguiente.cliente.getCedula()) > 0) {
                actual = actual.siguiente;
        }
        //actua para cuadrar en medio de los nodos si no se inserto al final o inicio.
        nuevo.siguiente = actual.siguiente;
        if (actual.siguiente != null) {
            actual.siguiente.anterior = nuevo;
        }
        //se ordenan los nodos
        actual.siguiente = nuevo;
        nuevo.anterior = actual;
    }
    }

    //muestra los datos de la lista ordenados
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
    
    //muestra los datos de la lista ordenados pero invertodos
    public void listarizq(){
        if (cabeza == null) {
            System.out.println("La lista está vacía.");
            return;
        }

        nodo actual = cabeza;

        
        while (actual.siguiente != null) {
            actual = actual.siguiente;
        }

        
        while (actual != null) {
            System.out.println("Cedula: " + actual.cliente.getCedula() + ", Nombre: " + actual.cliente.getNombre()); 
            actual = actual.anterior;
        }
    }}
