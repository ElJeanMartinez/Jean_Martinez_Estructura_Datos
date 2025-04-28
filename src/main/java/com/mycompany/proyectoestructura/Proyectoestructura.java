/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.proyectoestructura;

/**
 *
 * @author Jean Martinez
 */
public class Proyectoestructura {
    public static void main(String[] args) {
        listaclientes modelo = new listaclientes();
        VistaClientes vista = new VistaClientes();
        ControladorClientes controlador = new ControladorClientes(modelo, vista);
        controlador.iniciar();
    }
}




