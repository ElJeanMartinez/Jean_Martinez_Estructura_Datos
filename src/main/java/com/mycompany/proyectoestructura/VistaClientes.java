/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.proyectoestructura;
import javax.swing.*;
/**
 *
 * @author Jean Martinez
 */
public class VistaClientes {

    public String mostrarMenu() {
        // Mostrar el menú y devolver la opción seleccionada
        return JOptionPane.showInputDialog(null, "--- MENÚ ---\n1. Insertar cliente\n2. Mostrar lista de clientes\n3. Mostrar lista invertida\n4. Salir\nElija una opción:");
    }

    public long pedirCedula() {
        String cedulaStr = JOptionPane.showInputDialog("Ingrese la cédula del cliente:");
        try {
            return Long.parseLong(cedulaStr);  // Retorna directamente un long
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Cédula inválida. Debe ser un número.");
            return -1;  // Retorna un valor indicativo de error
        }
    }

    public String pedirNombre() {
        return JOptionPane.showInputDialog("Ingrese el nombre del cliente:");
    }

    public void mostrarListaClientes(String lista) {
        // Usamos JOptionPane para mostrar la lista de clientes
        JOptionPane.showMessageDialog(null, lista, "Lista de Clientes", JOptionPane.INFORMATION_MESSAGE);
    }

    public void mostrarMensaje(String mensaje) {
        JOptionPane.showMessageDialog(null, mensaje);
    }
}


