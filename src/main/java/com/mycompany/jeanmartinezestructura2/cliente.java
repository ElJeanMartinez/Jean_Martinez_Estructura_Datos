/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.jeanmartinezestructura2;

/**
 *
 * @author Estudiante
 */
//guarda los datos del cliente
public class cliente {
    private String cedula;
    private String nombre;

    public cliente(String cedula, String nombre) {
        this.cedula = cedula;
        this.nombre = nombre;
    }

    public String getCedula() {
        return cedula;
    }

    public String getNombre() {
        return nombre;
    }

    @Override
    public String toString() {
        return "Cedula: " + cedula + ", Nombre: " + nombre;
    }
}
