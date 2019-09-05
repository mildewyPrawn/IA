using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Controlador : MonoBehaviour
{
    // Idealmente sólo se requiere de sensores y actuadores para programar el comportamiento
    private Actuadores actuador;
    private Sensores sensor;
    private Rigidbody rb;

    // Variables globales porque para algo han de servir
    private float maxAltura;
    public float cargaX;
    public float cargaY;
    public float cargaZ;
    public float lastX;
    public float lastY;
    public float lastZ;

    public bool cargando;

    private Vector3 ultimaPosicion;

    // Asignaciones de componentes
    void Start(){
        actuador = GetComponent<Actuadores>();
        sensor = GetComponent<Sensores>();
        this.cargaX = actuador.getCargaX();
        this.cargaY = actuador.getCargaY();
        this.cargaZ = actuador.getCargaZ();
        this.lastX = actuador.getLastX();
        this.lastY = actuador.getLastY();
        this.lastX = actuador.getLastZ();

        cargando = false;
    }



    // Update y FixedUpdate son similares en uso, pero por regla general se recomienda usar
    // FixedUpdate para calcular elementos físicos como el uso de Rigidbody
    void FixedUpdate(){

        // El agente no realiza ninguna acción si no tiene batería
        if(sensor.Bateria() <= actuador.bateria.bateriaMinima) {

            actuador.Detener();
            actuador.goTo(cargaX, cargaY, cargaZ);
            return;
        }

        // A continuación se muestran ejemplos de uso de actuadores y sensores
        // para ser utilizados de manera manual (por una persona):
        // Acciones por si hay pared
        if (actuador.HayPared()) {
            actuador.Detener();
            actuador.Izquierda();
            actuador.Detener();
            actuador.Girar180();
            // Acciones por si no hay pared y toca un edificio
        } else if (sensor.TocandoEdificio()) {
            actuador.Ascender();
            actuador.Detener();
            // Accines sino toca nada.
        } else {
            actuador.Adelante();
        }
        actuador.Flotar(); //siempre flota
        //siempre calcula sus coordenadas
        actuador.setLastX(); 
        actuador.setLastY();
        actuador.setLastZ();
    }

// Método para girar 180
    void Girar180() {
        if(actuador.HayPared()){
            actuador.Detener();
            actuador.Girar180();
        }else{
            actuador.Adelante();
        }
    }
}
