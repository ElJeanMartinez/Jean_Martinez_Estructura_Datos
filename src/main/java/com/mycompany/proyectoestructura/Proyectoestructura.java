/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.proyectoestructura;
import java.util.Scanner;

/**
 *
 * @author Jean Martinez
 */
import java.util.Scanner;

public class Proyectoestructura {

    public static void main(String[] args) {
        listaclientes lista = new listaclientes();
        Scanner sc = new Scanner(System.in);
        int opcion;

        while (true) {
            System.out.println("\n--- MENU ---");
            System.out.println("1. Insertar cliente");
            System.out.println("2. Lista de clientes");
            System.out.println("3. Salir");
            System.out.print("Elija una opcion: ");
            opcion = sc.nextInt();
            sc.nextLine(); // Limpiar buffer

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese cedula: ");
                    String cedula = sc.nextLine();
                    System.out.print("Ingrese nombre: ");
                    String nombre = sc.nextLine();
                    lista.insertarOrdenado(new cliente(cedula, nombre));
                    break;
                case 2:
                    System.out.println("\n--- Lista de Clientes ---");
                    lista.listar();
                    break;
                case 3:
                    System.out.println("Aplicación finalizada.");
                    return; // Termina el programa
                default:
                    System.out.println("Opción invalida.");
            }
        }
    }
}


