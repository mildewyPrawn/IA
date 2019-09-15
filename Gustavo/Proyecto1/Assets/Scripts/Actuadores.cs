using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Actuadores : MonoBehaviour
{
    public Rigidbody rb; // Componente para simular acciones físicas realistas
    public Bateria bateria; // Componente adicional (script) que representa la batería
    private Sensores sensor; // Componente adicional (script) para obtener información de los sensores

    private float upForce; // Indica la fuerza de elevación del dron
    private float movementForwardSpeed = 250.0f; // Escalar para indicar fuerza de movimiento frontal
    private float wantedYRotation; // Auxiliar para el cálculo de rotación
    private float currentYRotation; // Auxiliar para el cálculo de rotación
    private float rotateAmountByKeys = 2.5f; // Auxiliar para el cálculo de rotación
    private float rotationYVelocity; // Escalar (calculado) para indicar velocidad de rotación
    private float sideMovementAmount = 2500.0f; // Escalar para indicar velocidad de movimiento lateral
    public float CargaX;
    public float CargaY;
    public float CargaZ;
    public float lastX;
    public float lastY;
    public float lastZ;

    float yRotation = 5.0f;

    //private Vector3 targetAngles;
    private Quaternion targetRotation;
    // Asignaciones de componentes
    void Start(){
        rb = GetComponent<Rigidbody>();
        sensor = GetComponent<Sensores>();
        bateria = GameObject.Find("Bateria").gameObject.GetComponent<Bateria>();
        // Coordenadas del centro de carga y últimas coordenadas.
        CargaX=rb.transform.position.x;
        CargaY=rb.transform.position.y;
        CargaZ=rb.transform.position.z;
        lastX=rb.transform.position.x;
        lastY=rb.transform.position.y;
        lastZ=rb.transform.position.z;
    }

    // ========================================
    // A partir de aqui, todos los métodos definidos son públicos, la intención
    // es que serán usados por otro componente (Controlador)

    public void Ascender(){
        upForce = 190;
        rb.AddRelativeForce(Vector3.up * upForce);
    }

    public void Descender(){
        upForce = 10;
        rb.AddRelativeForce(Vector3.up * upForce);
    }

    public void Flotar(){
        upForce = 98.1f;
        rb.AddRelativeForce(Vector3.up * upForce);
    }


    // Setters de las últimas coordenadas
    public void setLastX(){
        this.lastX = rb.transform.position.x;
    }

    public void setLastY(){
        this.lastY = rb.transform.position.y;
    }

    public void setLastZ(){
        this.lastZ = rb.transform.position.z;
    }

    // Getters de las últimas coordenadas
    public float getLastX(){
        return this.lastX;
    }

    public float getLastY(){
        return this.lastY;
    }

    public float getLastZ(){
        return this.lastZ;
    }

    // Getters de las coordenadas del centro de carga
    public float getCargaX(){
        return this.CargaX;
    }

    public float getCargaY(){
        return this.CargaY;
    }

    public float getCargaZ(){
        return this.CargaZ;
    }

    public void Adelante(){
        rb.AddRelativeForce(Vector3.forward * movementForwardSpeed);
    }

    public void Atras(){
        rb.AddRelativeForce(Vector3.back * movementForwardSpeed);
    }

    public void GirarDerecha(){
        rb.rotation = Quaternion.Euler(new Vector3(rb.rotation.x, rb.rotation.y + 90, rb.rotation.z));
    }

    // Método para girar 180 grados
    public void Girar180() {
        if(sensor.ParedNorte()){
            rb.rotation = Quaternion.Euler(new Vector3(rb.rotation.x,180.0f, rb.rotation.z));
            Derecha();
            Detener();
        }
        if(sensor.ParedSur()){
            rb.rotation = Quaternion.Euler(new Vector3(rb.rotation.x,0f, rb.rotation.z));
            Izquierda();
            Detener();
        }
        if(sensor.ParedEste()){
            rb.rotation = Quaternion.Euler(new Vector3(rb.rotation.x,270.0f, rb.rotation.z));
            Detener();
        }

        if(sensor.ParedOeste()){
            rb.rotation = Quaternion.Euler(new Vector3(rb.rotation.x,90.0f, rb.rotation.z));
            Detener();
        }

    }

    // Método que nos dice si hay una pared usando sensores de todas las paredes.
    public bool HayPared(){
        return((sensor.ParedNorte())||(sensor.ParedSur())||(sensor.ParedEste())||(sensor.ParedOeste()));
    }

    public void Avanzar() {
        transform.position += new Vector3 (3 * Time.deltaTime, 0, 0);

    }

    public void GirarIzquierda(){
        wantedYRotation -= rotateAmountByKeys;
        currentYRotation = Mathf.SmoothDamp(currentYRotation, wantedYRotation, ref rotationYVelocity, 0.25f);
        rb.rotation = Quaternion.Euler(new Vector3(rb.rotation.x, currentYRotation, rb.rotation.z));
    }

    public void Derecha(){
        rb.AddRelativeForce(Vector3.right * sideMovementAmount);
    }

    public void Izquierda(){
        rb.AddRelativeForce(Vector3.left * sideMovementAmount);
    }

    public void Detener(){
        rb.velocity = Vector3.zero;
        rb.angularVelocity = Vector3.zero;
    }

    public void Limpiar(GameObject basura) {
        basura.SetActive(false);
        sensor.SetTocandoBasura(false);
        sensor.SetCercaDeBasura(false);
    }

    public void CargarBateria() {
        bateria.Cargar();
    }

    // Método que va a cargar con las coordenadas del centro y las últimas visitadas
    public void VeACargar(float x, float y, float z,
                          float x1, float y1, float z1) {
        this.Detener();
        if(bateria.bateria < bateria.capacidadMaximaBateria)
            goTo(x,y,z);
        goTo(lastX, lastY, lastZ);
    }

    // Método de transporte a las coordenadas dadas.
    public void goTo(float x,float y, float z){
        rb.MovePosition(new Vector3(x,y,z)*Time.deltaTime);

    }
    
    public void regresaDeCarga(float x,float y, float z){

    }

}
