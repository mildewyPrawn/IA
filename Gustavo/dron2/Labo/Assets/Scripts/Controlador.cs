using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Controlador : MonoBehaviour
{
    // Idealmente sólo se requiere de sensores y actuadores para programar el comportamiento
    private Actuadores actuador;
    private Sensores sensor;
    
    // Variables globales porque para algo han de servir
    private float maxAltura;
    private Rigidbody rigidbody;
    private Vector3 ultimaPosicion;
    private bool movedBack;
    private bool movedFront;
    private bool direccion;
    // Asignaciones de componentes
    void Start(){
        actuador = GetComponent<Actuadores>();
        sensor = GetComponent<Sensores>();
        direccion=false;
        rigidbody=actuador.rb.GetComponent<Rigidbody>();
        movedFront=false;
        movedBack=true;
    }

    // Update y FixedUpdate son similares en uso, pero por regla general se recomienda usar
    // FixedUpdate para calcular elementos físicos como el uso de Rigidbody
    void FixedUpdate(){
        actuador.Flotar(); //siempre flota
        // El agente no realiza ninguna acción si no tiene batería
      /**  if(sensor.Bateria() <= 25) {
            ultimaPosicion = sensor.Ubicacion();
            actuador.VeACargar();
            Debug.Log(ultimaPosicion);
            
        } */
        
        // A continuación se muestran ejemplos de uso de actuadores y sensores
        // para ser utilizados de manera manual (por una persona):
        if (sensor.FrenteAPared()) {
            actuador.Detener();
            actuador.back(movedBack);
            Debug.Log(movedBack);
            Debug.Log(movedFront);    
            movedFront=false;
            movedBack=true;
            actuador.Detener();
            actuador.Flotar();
            actuador.Avanzar(movedFront, movedBack);

           return;
        } else if(sensor.ParedAtras()){
            actuador.Detener();
            actuador.front(movedFront);
            Debug.Log(movedBack);
            Debug.Log(movedFront);    
            movedBack=true;
            movedFront=false;
            actuador.Detener();
            actuador.Flotar();
            actuador.Avanzar(movedFront, movedBack);

            return;
        }else if (sensor.TocandoEdificio()) {
            actuador.Ascender();
            actuador.Detener();
            Debug.Log("EEdiifiiciioo");
            
        } else {
            actuador.Avanzar(movedFront , movedBack);
            Debug.Log("Naadaa");
            
        }

        
    }
}
