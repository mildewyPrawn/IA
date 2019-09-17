﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sensores : MonoBehaviour
{
    private GameObject basura; // Auxiliar para guardar referencia al objeto
    private Radar radar; // Componente auxiliar (script) para utilizar radar esférico
    private Rayo rayo; // Componente auxiliar (script) para utilizar rayo lineal
    private Bateria bateria; // Componente adicional (script) que representa la batería
    private Actuadores actuador; // Componente adicional (script) para obtener información de los ac

    // Banderas para todas las paredes.
    private bool tocandoParedNorte;
    private bool tocandoParedSur;
    private bool tocandoParedEste;
    private bool tocandoParedOeste;// Bandera auxiliar para mantener el estado en caso de tocar pared
    private bool cercaPared; // Bandera auxiliar para mantener el estado en caso de estar cerca de una pared
    private bool tocandoBasura; // Bandera auxiliar para mantener el estado en caso de tocar basura
    private bool cercaBasura; // Bandera auxiliar para mantener el estado en caso de estar cerca de una basura

    private bool tocandoEdificio; // Bandera para tocar edificios.

    // Asignaciones de componentes
    void Start(){
        radar = GameObject.Find("Radar").gameObject.GetComponent<Radar>();
        rayo = GameObject.Find("Rayo").gameObject.GetComponent<Rayo>();
        bateria = GameObject.Find("Bateria").gameObject.GetComponent<Bateria>();
        actuador = GetComponent<Actuadores>();
    }

    // ========================================
    // Los siguientes métodos permiten la detección de eventos de colisión
    // que junto con etiquetas de los objetos permiten identificar los elementos
    // La mayoría de los métodos es para asignar banderas/variables de estado.

    void OnCollisionEnter(Collision other){
        // Colisiones para todas las paredes
        if(other.gameObject.CompareTag("ParedNorte"))
            tocandoParedNorte = true;
        if(other.gameObject.CompareTag("ParedSur"))
            tocandoParedSur = true;
        if(other.gameObject.CompareTag("ParedEste"))
            tocandoParedEste = true;
        if(other.gameObject.CompareTag("ParedOeste"))
            tocandoParedOeste = true;
        if (other.gameObject.CompareTag("Edificio"))
            tocandoEdificio = true;
    }

    void OnCollisionStay(Collision other){
        if(other.gameObject.CompareTag("ParedNorte"))
            tocandoParedNorte = true;
        if(other.gameObject.CompareTag("ParedSur"))
            tocandoParedSur = true;
        if(other.gameObject.CompareTag("ParedEste"))
            tocandoParedEste = true;
        if(other.gameObject.CompareTag("ParedOeste"))
            tocandoParedOeste = true;
        if(other.gameObject.CompareTag("BaseDeCarga"))
            actuador.CargarBateria();
        if (other.gameObject.CompareTag("Edificio"))
            tocandoEdificio = true;
    }

    void OnCollisionExit(Collision other){
        if(other.gameObject.CompareTag("ParedNorte"))
            tocandoParedNorte = false;
        if(other.gameObject.CompareTag("ParedSur"))
            tocandoParedSur = false;
        if(other.gameObject.CompareTag("ParedEste"))
            tocandoParedEste = false;
        if(other.gameObject.CompareTag("ParedOeste"))
            tocandoParedOeste = false;
        if (other.gameObject.CompareTag("Edificio"))
            tocandoEdificio = false;
    }

    void OnTriggerEnter(Collider other){
        if(other.gameObject.CompareTag("Basura")){
            tocandoBasura = true;
            basura = other.gameObject;
        }
                    
            
    }

    void OnTriggerStay(Collider other){
        if(other.gameObject.CompareTag("Basura")){
            tocandoBasura = true;
            basura = other.gameObject;
        }
    }

    void OnTriggerExit(Collider other){
        if(other.gameObject.CompareTag("Basura")){
            tocandoBasura = false;
            actuador.Limpiar(other.gameObject);
        }
    }

    // ========================================
    // Los siguientes métodos definidos son públicos, la intención
    // es que serán usados por otro componente (Controlador)

    public bool ParedNorte(){
        return tocandoParedNorte;
    }
    public bool ParedSur(){
        return tocandoParedSur;
    }
    public bool ParedEste(){
        return tocandoParedEste;
    }
    public bool ParedOeste(){
        return tocandoParedOeste;
    }
    public bool CercaDePared(){
        return radar.CercaDePared();
    }

    public bool FrenteAPared(){
        return rayo.FrenteAPared();
    }

    public bool TocandoEdificio() {
        return tocandoEdificio;
    }

    public bool CercaDeEdificio(){
        return radar.CercaDeEdificio();
    }

    public bool FrenteAEdificio(){
        return rayo.FrenteAEdificio();
    }

    public bool TocandoBasura(){
        return tocandoBasura;
    }

    public GameObject Basurita() {
        return this.basura;
    }

    public bool CercaDeBasura(){
        return radar.CercaDeBasura();
    }

    public float Bateria(){
        return bateria.NivelDeBateria();
    }

    // Algunos otros métodos auxiliares que pueden ser de apoyo

    public GameObject GetBasura(){
        return basura;
    }

    public Vector3 Ubicacion(){
        return transform.position;
    }

    public void SetTocandoBasura(bool value){
        tocandoBasura = value;
    }

    public void SetCercaDeBasura(bool value){
        radar.setCercaDeBasura(value);
    }
}