﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Componente auxiliar para genera rayos que detecten colisiones de manera lineal
// En el script actual se dibuja y comprueban colisiones con un rayo al frente del objeto
// sin embargo, es posible definir más rayos de la misma manera.
public class Rayo : MonoBehaviour
{
    public float longitudDeRayo;
    private bool frenteAPared;
    private bool frenteAEdificio;

    void Update(){
        // Se muestra el rayo únicamente en la pantalla de diseño (Scene)
        Debug.DrawLine(transform.position, transform.position + (transform.forward * longitudDeRayo), Color.blue);
    }

    void FixedUpdate(){
        // Similar a los métodos OnTrigger y OnCollision, se detectan colisiones con el rayo:
        RaycastHit raycastHit;
        if(Physics.Raycast(transform.position, transform.forward, out raycastHit, longitudDeRayo)){
            if(raycastHit.collider.gameObject.CompareTag("Pared")){
                frenteAPared = true;
                return;
            }
            else{
                frenteAPared = false;
                return;
            }
            if (raycastHit.collider.gameObject.CompareTag("Edificio")) {
                frenteAEdificio = true;
                return;
            } else {
                frenteAEdificio = false;
                return;
            }
        }
    }

    // Ejemplo de métodos públicos que podrán usar otros componentes (scripts):
    public bool FrenteAPared(){
        return frenteAPared;
    }
    public void ParedEvitada(){
        frenteAPared=false;
    }
    public bool FrenteAEdificio() {
        return frenteAEdificio;
    }
}
