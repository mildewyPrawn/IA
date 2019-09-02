﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Controlador : MonoBehaviour
{
    // Idealmente sólo se requiere de sensores y actuadores para programar el comportamiento
    private Actuadores actuador;
    private Sensores sensor;

    // Variables globales porque para algo han de servir
    private float maxAltura;

    private Vector3 ultimaPosicion;

    // Asignaciones de componentes
    void Start(){
        actuador = GetComponent<Actuadores>();
        sensor = GetComponent<Sensores>();
    }

    // Update y FixedUpdate son similares en uso, pero por regla general se recomienda usar
    // FixedUpdate para calcular elementos físicos como el uso de Rigidbody
    void FixedUpdate(){

        // El agente no realiza ninguna acción si no tiene batería
        if(sensor.Bateria() <= 25) {
            ultimaPosicion = sensor.Ubicacion();
            actuador.VeACargar();
            Debug.Log(ultimaPosicion);
            return;
        }
        
        // A continuación se muestran ejemplos de uso de actuadores y sensores
        // para ser utilizados de manera manual (por una persona):
        if (sensor.TocandoPared()) {
            actuador.Detener();
            actuador.Girar180();
            actuador.Adelante();
            Debug.Log("Paareed");
        } else if (sensor.TocandoEdificio()) {
            actuador.Ascender();
            actuador.Detener();
            Debug.Log("EEdiifiiciioo");
        } else {
            actuador.Adelante();
            Debug.Log("Naadaa");
        }

        actuador.Flotar(); //siempre flota
    }
}