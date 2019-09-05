﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Componente auxiliar que modela el comportamiento de una bateria interna
// Dicha batería se descarga constantemente a menos que se utilize un método para recargar
public class Bateria : MonoBehaviour
{
    public float bateriaMinima = 5;
    public float bateria; // Esta cifra es equivalente a los segundos activos de la batería
    public float capacidadMaximaBateria; // Indica la capacidad máxima de la batería
    public float velocidadDeCarga; // Escalar para multiplicar la velocidad de carga de la batería
    public bool cargando = false;

    void Update(){
        if(bateria > 0) // esto evita que la batería sea negativa
            bateria -= Time.deltaTime;
    }

    // ========================================
    // Métodos públicos que podrán ser utilizados por otros componentes (scripts):
    public void Cargar(){
        if(bateria < capacidadMaximaBateria + 2) {
            bateria += Time.deltaTime * velocidadDeCarga;
          } else {
            //cargando = false;
      }
    }

    public float NivelDeBateria(){
        return bateria;
    }
}
