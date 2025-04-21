/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.jeanmartinezestructura2;
import java.util.Scanner;

/**
 *
 * @author Jean Martinez
 */
import java.util.Scanner;

public class JeanMartinezEstructura2 {

    public static void main(String[] args) {
        
        //instancia de la listaclientes, representa el doble enlace
        listaclientes lista = new listaclientes();
        Scanner sc = new Scanner(System.in);
        int opcion;
        
        //ciclo menu
        while (true) {
            System.out.println("\n--- MENU ---");
            System.out.println("1. Insertar cliente");
            System.out.println("2. Lista de clientes");
            System.out.println("3. Lista Invertida");
            System.out.println("4. Salir");
            System.out.print("Elija una opcion: ");
            //limpia el buffer
            opcion = sc.nextInt();
            sc.nextLine(); 

            //switch para realizar la opcion marcada
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
                    System.out.println("\n--- Lista de Clientes invertida ---");
                    lista.listarizq();
                    break;
                case 4:
                    System.out.println("Aplicacion finalizada.");
                    return; 
                default:
                    System.out.println("Opcion invalida.");
            }
        }
    }
}