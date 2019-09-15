using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Componente auxiliar que utiliza un Collider esférico a manera de radar
// para comprobar colisiones con otros elementos.
// Las comprobaciones y métodos son análogos al componente (script) de Sensores.
public class Radar : MonoBehaviour
{
    private bool cercaDeBasura;
    private bool cercaDePared;
    private bool cercaDeEdificio;

    void OnTriggerEnter(Collider other){
        if(other.gameObject.CompareTag("Basura")){
            cercaDeBasura = true;
        }
        if(other.gameObject.CompareTag("Pared")){
            cercaDePared = true;
        }
        if (other.gameObject.CompareTag("Edificio")) {
            cercaDeEdificio = true;
        }
    }

    void OnTriggerStay(Collider other){
        if(other.gameObject.CompareTag("Basura")){
            cercaDeBasura = true;
        }
        if(other.gameObject.CompareTag("Pared")){
            cercaDePared = true;
        }
        if (other.gameObject.CompareTag("Edificio")) {
            cercaDeEdificio = true;
        }
    }

    void OnTriggerExit(Collider other){
        if(other.gameObject.CompareTag("Basura")){
            cercaDeBasura = false;
        }
        if(other.gameObject.CompareTag("Pared")){
            cercaDePared = false;
        }
        if (other.gameObject.CompareTag("Edificio")) {
            cercaDeEdificio = false;
        }
    }

    public bool CercaDeBasura(){
        return cercaDeBasura;
    }

    public bool CercaDePared(){
        return cercaDePared;
    }

    public bool CercaDeEdificio() {
        return cercaDeEdificio;
    }

    public void setCercaDeBasura(bool value){
        cercaDeBasura = value;
    }
}
