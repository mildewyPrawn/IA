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

    public void setLastX(){
        this.lastX = rb.transform.position.x;
    }

    public void setLastY(){
        this.lastY = rb.transform.position.y;
    }
    public void setLastZ(){
        this.lastZ = rb.transform.position.z;
    }
    public float getLastX(){
        return this.lastX;
    }


    public float getLastY(){
        return this.lastY;
    }


    public float getLastZ(){
        return this.lastZ;
    }


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
        //rb.rotation = new Vector3 (0, 180.0f, 0);
        /*
          Detener();
          Debug.Log("VOY PARA ATRÁS 1");
          Atras();
          Detener();
          Debug.Log("VOY PARA ATRÁS 2");
          Atras();
          Debug.Log("VOY A GIRAR 180 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
          GirarDerecha();
          Detener();
          Adelante();
          Detener();
          GirarDerecha();
        */
    }
    public bool HayPared(){
        return((sensor.ParedNorte())||(sensor.ParedSur())||(sensor.ParedEste())||(sensor.ParedOeste()));
    }
    /*
      Debug.Log(rb.rotation.y);
      Debug.Log(rb.rotation.y);
      Debug.Log("valor");
      Debug.Log((rb.rotation.y + 180) % 360);
      rb.rotation.y = rb.rotation.y + 180f % 360;

      var degreesPerSecond = 30.0;

      transform.Rotate (Vector3.up * degreesPerSecond * Time.deltaTime);
    */
    //transform.rotation.y=180;

    //  Debug.Log(transform.rotation.y);
    //transform.rotation = Quaternion.Euler(new Vector3(transform.rotation.x, transform.rotation.y + 180.0f, transform.rotation.z));


    //float smooth = 5.0f;
    //float tiltAngle = 180.0f;
    // Smoothly tilts a transform towards a target rotation.
    //float tiltAroundZ = Input.GetAxis("Horizontal") * tiltAngle;
    //float tiltAroundX = Input.GetAxis("Vertical") * tiltAngle;
    /*
    // Rotate the cube by converting the angles into a quaternion.
    Debug.Log((float)transform.rotation.y);
    Quaternion target = Quaternion.Euler(0.0f, transform.rotation.y + 180.0f, 0.0f);
    transform.rotation = Quaternion.Slerp(transform.rotation, target,  Time.deltaTime * smooth);
    */
    //float yRotation = 180.0f;
    /*
    //yRotation += transform.rotation.y;
    transform.eulerAngles = new Vector3(transform.rotation.x, yRotation, transform.rotation.z);
    //yRotation += Input.GetAxis("Horizontal");
    //transform.eulerAngles = new Vector3(10, yRotation, 0);

    rb.transform.rotation = Quaternion.FromToRotation((rb as DistanceMeasuramentVisualization3D).GetCurrentDirection(), globalPositionEnd - start.GlobalPosition)*rb.transform.rotation);


    //Vector3 targetAngles;
    //    targetAngles = transform.eulerAngles + 180f * Vector3.up; // what the new angles should be

    // transform.eulerAngles = Vector3.Lerp(transform.eulerAngles, targetAngles, 1 * Time.deltaTime);
    //transform.Rotate(Vector3.up, -180);
    //rb.rotation = Quaternion.Euler(new Vector3(rb.rotation.x, currentYRotation + 180f, rb.rotation.z));
    //targetRotation = Quaternion.LookRotation(-transform.forward, Vector3.up);

    //   transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, 1f * Time.deltaTime);*/


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

    public void VeACargar(float x, float y, float z,
                          float x1, float y1, float z1) {
        this.Detener();
        Debug.Log("LA XXXXXXXXXXXXXXXXXXXXXXXX");
        Debug.Log(x1);
        Debug.Log("LA YYYYYYYYYYYYYYYYYYY");

        Debug.Log(y1);
        Debug.Log("LA ZZZZZZZZZZZZZZZZZZZZZZZ");

        Debug.Log(z1);

        if(bateria.bateria < bateria.capacidadMaximaBateria)
            goTo(x,y,z);
        //this.Detener();
        goTo(lastX, lastY, lastZ);
        //    this.Adelante();
        //    this.GirarDerecha();
        //  this.Descender();
        //  this.CargarBateria();
    }
    public void goTo(float x,float y, float z){
        rb.MovePosition(new Vector3(x,y,z)*Time.deltaTime);

    }
    public void regresaDeCarga(float x,float y, float z){

    }

}
