/**
   Interface con los metodos necesarios para implementar el metodo
   de recocido simulado junto con la solucion a un problema particular.

   @author Benjamin Torres
   @version 0.1
*/
package recocido;

public class RecocidoSimulado{
    float temperatura;
    float valor;
    float decaimiento;


    /**
       Inicializa los valores necesarios para realizar
       recocido simulado durante un numero determinado de iteraciones
    */
    public RecocidoSimulado(){ //escoge los parametros necesarios para inicializar el algoritmo

    }

    /**
       Funcion que calcula una nueva temperatura en base a
       la anterior y el decaemiento usado.
       @param temperatura, float con el valor actual
       @param decaimiento, float que sera usado para hacer decaer el valor de temperatura
       @return nueva temperatura
    */
    public float nuevaTemperatura(float temperatura,float decaimiento){
        return 0;
    }

    /**
       Genera y devuelve la solucion siguiente dependiendo de su valor
       y de la probabilidad de elegir una solucion peor
       @param Solucion que sera usada como base para elegir a la siguiente
       @return Solucion nueva
    */
    public Solucion seleccionarSiguienteSolucion(Solucion s){
        return new Solucion();
    }

    /**
       Ejecuta el algoritmo con los parametros con los que fue inicializado
       devuelve una solucion.
       @param
       @return Solucion al problema
    */
    public Solucion ejecutar(){
        return new Solucion();
    }
}
