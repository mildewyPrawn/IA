﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Componente auxiliar para genera rayos que detecten colisiones de manera lineal
// En el script actual se dibuja y comprueban colisiones con un rayo al frente del objeto
// sin embargo, es posible definir más rayos de la misma manera.
public class RayoAtras : MonoBehaviour
{
    public float longitudDeRayo;
    private bool ParedAtras;
    private bool EdificioAtras;

    void Update(){
        // Se muestra el rayo únicamente en la pantalla de diseño (Scene)
        Debug.DrawLine(transform.position, transform.position + (transform.forward) * longitudDeRayo, Color.blue);
    }

    void FixedUpdate(){
        // Similar a los métodos OnTrigger y OnCollision, se detectan colisiones con el rayo:
        RaycastHit raycastHit;
        if(Physics.Raycast(transform.position, transform.forward, out raycastHit, longitudDeRayo)){
            if(raycastHit.collider.gameObject.CompareTag("Pared")){
                ParedAtras = true;
                return;
            }
            else{
                ParedAtras = false;
                return;
            }
            if (raycastHit.collider.gameObject.CompareTag("Edificio")) {
                EdificioAtras = true;
                return;
            } else {
                EdificioAtras = false;
                return;
            }
        }
    }

    // Ejemplo de métodos públicos que podrán usar otros componentes (scripts):
    public bool HayParedAtras(){
        return ParedAtras;
    }
    public void ParedEvitada(){
        ParedAtras=false;
    }
    public bool HayEdificioAtras() {
        return EdificioAtras;
    }
}
