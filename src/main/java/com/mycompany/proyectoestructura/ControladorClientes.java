/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.proyectoestructura;

public class ControladorClientes {

    private listaclientes modelo;
    private VistaClientes vista;

    public ControladorClientes(listaclientes modelo, VistaClientes vista) {
        this.modelo = modelo;
        this.vista = vista;
    }

    public void iniciar() {
        String opcion;

        do {
            opcion = vista.mostrarMenu();

            switch (opcion) {
                case "1":
                    long cedula = vista.pedirCedula(); // Ahora ya retorna un long directamente
                    if (cedula == -1) {
                        break; // Si la cédula es inválida (valor -1), no seguimos
                    }
                    String nombre = vista.pedirNombre();
                    modelo.insertarOrdenado(new cliente(cedula, nombre));
                    vista.mostrarMensaje("Cliente insertado con éxito.");
                    break;

                case "2":
                    StringBuilder lista = new StringBuilder();
                    nodo actual = modelo.getCabeza();
                    if (actual == null) {
                        lista.append("Lista vacía.");
                    } else {
                        while (actual != null) {
                            lista.append(actual.cliente).append("\n");
                            actual = actual.siguiente;
                        }
                    }
                    vista.mostrarListaClientes(lista.toString());
                    break;

                case "3":
                    String listaInversa = modelo.listarInverso(); // Obtener la lista en orden inverso
                    vista.mostrarListaClientes(listaInversa); // Mostrarla en la vista
                    break;

                case "4":
                    vista.mostrarMensaje("Aplicación finalizada.");
                    break;

                default:
                    vista.mostrarMensaje("Opción inválida.");
            }

        } while (!opcion.equals("4"));
    }
}

