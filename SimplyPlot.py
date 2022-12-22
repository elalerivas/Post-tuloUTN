import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #importo para trabajar con tablas
from sympy import *
#from streamlit_option_menu import option_menu
#import math
x, y, z, t = symbols('x y z t')
a, b, c,d,e,k,l,m, n,o, p,q,r,s,u,v,w = symbols('a b c d e k l m n o p q r s u v w')
#######################################################
"""
## **SimplePlot 2D**
"""
with st.sidebar:
        #selected = option_menu("Menú de Opciones", ["Home", 'Configuraciones'],
        #icons=['house', 'gear'], menu_icon="cast", default_index=1)
        #selected
        ################      Diccionarios        #####################################################################
        colores=['azul', 'verde', 'rojo', 'cian', 'magenta', 'amarillo', 'negro', 'blanco']
        dicColor={'rojo':'r','azul':'b','verde':'g','cian':'c','magenta':'m','amarillo':'y','negro':'k','blanco':'w'}
        """## Opciones de Gráfico"""
        estilos=['ninguna','solido', 'trazos', 'rayapunto', 'punteada']
        dicEstilo={'ninguna':'','solido':'-', 'trazos':'--', 'rayapunto':'-.', 'punteada':'dotted'}
        ## reemplazo de funciones matemáticas
        func_orig=['pow','PI','sqrt','exp','log','ln','sin','cos','tan','asin','acos','atan','hsin','hcos','htan','abs']
        reemplazo=['np.power','np.pi','np.sqrt','np.exp','np.log10','np.log','np.sin','np.cos','np.tan','np.asin',      
                                                                'np.acos','np.atan','np.sinh','np.cosh','np.tanh','np.absolute']
        # Parámetros
        with st.expander('Parámetros'):
                [a, b, c,d,e,k,l,m, n,o, p,q,r,s,u,v,w] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                #parametrotext=['a','b','c','d','e','k','l','m','n','o','p','q','r','s','u','v','w']
                parametro=''
                parametro=st.text_area('Defina los parámetros (ej. a= 2.3 b=-1)')
                
                st.latex('\\tiny'+latex(parametro))
                
                for i in range (len(func_orig)):
                        
                        parametro=parametro.replace(func_orig[i],reemplazo[i])
                def comas(param):
                        coma=param.count(',')
                        if Mod(coma,2)!=0:
                                st.write('Definición no equilibrada')
                comas(parametro)
                
                #parametros=[a, b, c,d,e,k,l,m, n,o, p,q,r,s,u,v,w]
                exec(f'{parametro}')
                st.write('a=', a,'b=',b, 'c=',c,'d=',d,'e=',e,'k=',k,'l=',l,'m=',m,
                'n=',n,'p=',p,'q=',q,'r=',r,'s=',s,'u=',u,'v=',v,'w=',w)

        #  Funciones
        with st.expander('Funciones'):  # Funciones

                # Función principal
                funcionf=st.text_input('Ingrese f(x)',placeholder='exp(-pow(x,2))*sin(5*x)')    
                if funcionf == '':
                        funcionf = 'exp(-pow(x,2))*sin(5*x)'
                visiblef=True
                col1,col2=st.columns(2)
                with col1:
                        leyenda=st.text_input('Leyenda',placeholder='i.e. f(x)')
                        estilo=st.selectbox('tipo de linea',estilos,index=1)
                        estilo=dicEstilo[estilo]
                with col2:
                        color=st.selectbox('color linea',colores,index=0)
                        color=dicColor[color]
                        ancholin=st.number_input('ancho linea',min_value=1, max_value=8,value=1,step=1)

                #  Función secundaria g(x)
                funciong=st.text_input('Ingrese g(x)')    
                if funciong == '':
                        es_g=False
                        visibleg=False
                else:
                        es_g=True
                        visibleg=True
                        
                col1,col2=st.columns(2)
                with col1:
                        leyendag=st.text_input('Leyenda ',placeholder='i.e.: g(x)')
                        estilog=st.selectbox('tipo de linea ',estilos,index=1)
                        estilog=dicEstilo[estilog]
                with col2:
                        colorg=st.selectbox('color linea ',colores,index=1)
                        colorg=dicColor[colorg]
                        ancholing=st.number_input('ancho linea ',min_value=1, max_value=8,value=1,step=1)
                
                #  Función secundaria h(x)
                funcionh=st.text_input('Ingrese h(x)')    
                if funcionh == '':
                        es_h=False
                        visibleh=False
                else:
                        es_h=True
                        visibleh=True

                col1,col2=st.columns(2)
                with col1:
                        leyendah=st.text_input('Leyenda.',placeholder='i.e. h(x)')
                        estiloh=st.selectbox('tipo de linea.',estilos,index=1)
                        estiloh=dicEstilo[estiloh]
                with col2:
                        colorh=st.selectbox('color linea.',colores,index=2)
                        colorh=dicColor[colorh]
                        ancholinh=st.number_input('ancho linea.',min_value=1, max_value=8,value=1,step=1)
                
        with st.expander('Dominio'):       #  Dominio de la función
                col1, col2= st.columns(2)
                with col1:
                         x0=st.number_input('xmin',value=-10.0, step=0.1)
                with col2:
                        xf=st.number_input('xmax',value=10.0, step=0.1)
                
                        resol=st.number_input('resolución',min_value=10, max_value=400,value=300, step=10)
        
        with st.expander('Área de gráfico'):  # Area de gráfico
                coloresff=['gris', 'amarillo', 'celeste', 'cian', 'verde', 'rosa', 'lila','lavanda', 'blanco']
                dicColorff={'gris':'lightgray','amarillo':'moccasin','celeste':'lightblue','cian':'lightcyan','verde':'aquamarine',
                'rosa':'mistyrose','lila':'plum','lavanda':'lavender','blanco':'w'}
                titulo=st.text_input('Título', placeholder=('Nombre del gráfico'))
                if titulo=='':
                        titulo='Título'
                
                col1, col2=st.columns(2)
                
                with col1:
                        
                        x_label=st.text_input('Absisas', placeholder=('x'))
                        if x_label=='':
                                x_label='x'
                        vImagen=st.slider('alto imagen',min_value=2, max_value=10,value=4,step=1)
                with col2:       
                        y_label=st.text_input('Ordenadas', placeholder=('y'))
                        if y_label=='':
                                y_label='y'
                        
                        color_borde=st.selectbox('color borde',coloresff,index=0)
                        color_borde=dicColorff[color_borde]
        
        
        #with st.expander('Marcas'):  # Marcas
        #        col1, col2=st.columns(2)
         #       with col1:
         #               marcas=['ninguna','punto', 'circulo', 'triangulo', 'cuadrado', 'estrella', 'exagono', 'cruz1', 'cruz2']
         ##       dicMarca={'ninguna':'','punto':'.', 'circulo':'o', 'triangulo':'^', 'cuadrado':'s', 'estrella':'*', 'exagono':'H', 'cruz1':'x', 'cruz2':'+'}
         #       marca=dicMarca[marca]  

         #       with col2:
                                
         #               #colorMark=st.color_picker('color')
         #               colorMark=st.selectbox('color marca',colores,index=0)
         #               #dicColor={'rojo':'r','azul':'b','verde':'g','cian':'c','magenta':'m','amarillo':'y','negro':'k','blanco':'w'}
         #               colorMark=dicColor[colorMark]
            
         #               SizeMarca=st.number_input('tamaño marca',min_value=1, max_value=8,value=2,step=1)

tab1, tab2, tab3 = st.tabs(['INICIO','FUNCIONES','Acerca de'])
with tab1:

    """
    **SimplePlot 2D** es un graficador sencillo que te permite,
    de una manera ágil e intuitiva, personalizar el área del gráfico, 
    dominio de la función, mostrar u ocultar ejes y divisiones,
    estilos de línea, colores y más.
    En la barra lateral se encuetra el menú de opciones, con el cual
    podrán personalizarse todos elementos del gráfico"""

    st.image('./Grafica 1.jpg','Fig. 1 Gráfico personalizado', width=600,use_column_width=20)
    """Al ingresar la función en formato de texto, ésta se mostrará
    en la ventana gráfica, y una vez terminada la personalización,
    podrá exportarse en formato de imagen haciendo click en el botón de descarga:"""
    col1,col2,col3=st.columns(3)
    with col2:
        st.image('./Boton descargar.jpg',"Fig.2 Botón de descarga")

    """
    ### Sintaxis para la introducción de funciones
    Deben ser funciones de una sola variable (*x*), aunque 
    también pueden contener parámetros que serán definidos por usuario, con valores constantes.
     

    A continuación se presenta una tabla con las funciones aceptadas:
    su nombre, y la sintaxis correspondiente:   

    
    """
    
    
    func_nombre=['lineal','cuadrática','valor absoluto', 'logaritmo natural','logaritmo de base 10','exponencial','raiz cuadrada',
            'potencial','signo','seno','coseno','tangente','arco seno','arco coseno','arco tangente',
            'seno hiperbólico','coseno hiperbólico','tangente hiperbólica']
    
    #func_expr=[a*x+b,a*pow(x,2)+b*x+c, log(x),log(x,n), exp(x), sqrt(x),pow(x,p),sign(x),
    #        sin(x), cos(x), tan(x), asin(x), acos(x), atan(x),sinh(x),cosh(x),tanh(x)]

    #func_latex=[latex(a*x+b),latex(a*pow(x,2)+b*x+c), latex(log(x)),latex(log(x,n)),latex(exp(x)), latex(sqrt(x)),
     #    latex(pow(x,p)),latex(sign(x)), latex(sin(x)), latex(cos(x)), latex(tan(x)), latex(asin(x)), latex(acos(x)),
     #    latex(atan(x)),latex(sinh(x)),latex(cosh(x)),latex(tanh(x))]

    func_texto=['a*x+b','a*pow(x,2)+b*x+c','absolute(x)','ln(x)','log(x)','exp(x)', 'sqrt(x)',
         'pow(x,p)','sign(x)', 'sin(x)', 'cos(x)', 'tan(x)', 'asin(x)', 'acos(x)',
         'atan(x)','sinh(x)','cosh(x)','tanh(x)']
    
    
    func_math=latex(a*pow(x,2))
    func_dic={'Función':func_nombre[0:8], 'Entrada':func_texto[0:8], 'Función ':func_nombre[8:16],'Entrada ':func_texto[8:16]}
    tabla1=pd.DataFrame(data=func_dic)
    tabla1
    #videos
    """#### Cómo introducir funciones    :point_down: (*ver video*) """
    #video1=open("./Videos/Video1.mp4","rb")
    st.video("https://youtu.be/g3bDNgY5KJs")

    """ ### Uso de parámetros
    **SimplePlot 2D** permite definir constantes a modo de parámetros en la sección correspondiente en la barra lateral.
    En el campo de texto pueden introducirse definiciones numéricas para las constantes ya definidas, 
    para lss cuales se han reservado las letras minúsculas (*a, b, c, ....*), exceptuando las letras *f, g,
    h, i, j, o, t, x, y, z*, para evitar confunciones.
    Estas ya tienen asignados los valores 0 (cero), a excepción de a que está inicializada con el valor 1 (uno).
    Existen dos formas de introducir los datos; uno es escribiendo la definición de cada parámetro en diferentes líneas,
    y otra, escribiendo en una misma línea varios parámetros separados por coma (,), y luego del signo igual (=),
    sus valores también separados por coma, como se muestra en la figura 3"""
    col1, col2 = st.columns(2)
    with col1:
        st.image('./imagen 3.jpg', 'Fig.3',width=250)
        """Para actualizar los valores, debe darse entrada con la combinación de las teclas **CTRL+ENTER**. 
        Se muestran en forma permanente los valores actuales de las constantes predefinidas.
        """
    with col2:
        st.image('./imagen 4.jpg','Fig.4', width=250)
# página de gráficas
    """
    Tambien se permite definir parámetros con cualquier nombre, exceptuando las palabras reservadas de *Python* y la letra '*x*',
    Aunque sus valores numéricos actuales no son mostrados como el de las predefinidas.
    Borrando el campo de texto y con **CRTL+ENTER**, se reinician los valores predefinidos.
    También se admiten operaciones matemáticas con los operadores y funciones usuales.
    """
    st.image('./imagen 5.jpg','Fig.5', width=250)

    """#### Ejemplo de uso de parámetros:  *Tiro oblicuo*
    Se definen las constantes v0: velocidad inicial*; y0: altura inicial;
    alfa: ángulo de disparo, en grados; y las componentes de v0, v0x y v0y;
    y se define la función del tiempo 'x', y, la altura, como:
    f(x) = y0 + v0y * x - 0.5 * gravedad * pow(x,2)
    """

    
    st.image('./imagen 8.jpg','Fig.6')
with tab2:
        
        def parentesis(func):
                parent=[func.count('('),func.count(')')]
                if parent[0] > parent[1]:
                        st.write('Revisar paréntesis. Falta " ) "')
                if parent[0] < parent[1]:
                        st.write('Revisar paréntesis. Falta " ( "')
                  
        # creo ventana gráfica
        
        ff=plt.figure(figsize=(9,vImagen),facecolor=color_borde,edgecolor='k')
        
        #ff.add_axes([0.1,0.5,0.5,0.5])
        #ax1=plt.subplot(331)      

              
        # Intervalo de dominio
        x=np.linspace(x0,xf,resol)
        visiblegrid=True
        visibleejes=True
        col1, col2,col3,col4,col5=st.columns(5)
        with col1:
                ocultaf=st.checkbox('Ocultar f(x)')
                if ocultaf:
                        visiblef=False
        with col2:
                ocultag=st.checkbox('Ocultar g(x)')  
                if ocultag:
                        visibleg=False     
        with col3:
                ocultah=st.checkbox('Ocultar h(x)') 
                if ocultah:
                        visibleh=False 
        with col4:
                ocultagrid=st.checkbox('Ocultar grilla') 
                if ocultagrid:
                        visiblegrid=False 
        with col5:
                ocultaejes=st.checkbox('Ocultar ejes') 
                if ocultaejes:
                        visibleejes=False 
        

        col1, col2, col3 = st.columns(3)     
        
        with col1: 
                parentesis(funcionf)
                funcionf0=funcionf # guarda sintaxis original
                st.latex('\small f(x) = '+latex(funcionf0))

                for i in range (0,len(func_orig)):
                        funcionf=funcionf.replace(func_orig[i],reemplazo[i])
        
        exec(f'funcion1={funcionf}')
        
        y1=funcion1
        #chequea si la función es una constante
        if(isinstance(y1,int) or isinstance(y1,float)):
                y1=[]
                for i in x:
                        y1.append(funcion1)
        
        ## Crear tabla a partir de f(x)
        #dicdatos={x:y1}
        tabladatos=pd.DataFrame(y1,x)

        graf=plt.plot(x,y1,visible=visiblef,c=color,ls= estilo ,lw=ancholin, label= leyenda)
        with col2: 

                parentesis(funciong)
                funciong0=funciong
                
                                                
                
                if(es_g==True):
                        st.latex('\small g(x) = '+latex(funciong0))
                        for i in range (0,len(func_orig)):
                                funciong=funciong.replace(func_orig[i],reemplazo[i])
                        exec(f'funcion2={funciong}')
                        y2=funcion2
                        #es_const(funcion2,y2)
                        if(isinstance(y2,int) or isinstance(y2,float)):
                                y2=[]
                                for i in x:
                                        y2.append(funcion2)
                        graf2=plt.plot(x,y2,visible=visibleg,c=colorg,ls= estilog ,lw=ancholing,label= leyendag)
        
        
        with col3:

                parentesis(funcionh)
                funcionh0=funcionh
                
                if(es_h==True):
                        st.latex('\small h(x) = '+latex(funcionh0))
                        for i in range (0,len(func_orig)):
                                funcionh=funcionh.replace(func_orig[i],reemplazo[i])
                        exec(f'funcion3={funcionh}')
                        y3=funcion3
                        if(isinstance(y3,int) or isinstance(y3,float)):
                                y3=[]
                                for i in x:
                                        y3.append(funcion3)
                        graf3=plt.plot(x,y3,visible=visibleh,c=colorh,ls= estiloh ,lw=ancholinh,label= leyendah)
        
        
        

        
        
        
        #plt.text(5, 0.5, r'$\mu=100,\ \sigma=15$')
        plt.legend() # para que se muestre los labels
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        #plt.axis([x0,xf,-100,100])
        plt.suptitle(titulo)
        #st.write(visiblegrid)
        if visiblegrid:
                plt.grid(color='grey',ls='--')
        plt.axhline(color='grey',lw=2,visible=visibleejes, label='x')
        plt.axvline(color='grey',lw=2,visible=visibleejes,label='y')
        #ax=ff.add_axes([0.1,0.1,0.8,0.8])
        #ax.set_xticks([0,2,4,6])
        #ax3=plt.subplot(333,sharex=ax1)
        #plt.plot(x,y,c=color,ls= estilo ,marker=marca,lw=ancholin,markersize=SizeMarca,mec=colorMark, label= leyenda)
        
        
        
        

        ff #muestra graficos
        plt.savefig('https://github.com/elalerivas/Post-tuloUTN/grafico23.png')
        col1,col2,col3,col4=st.columns(4)
        
        with col4:
                def guardarimagen():
                      plt.savefig('https://github.com/elalerivas/Post-tuloUTN/graficoviejo.png')  
                with open('.\grafico.png', 'rb') as archivo:
                        descargar=st.download_button('Descargar gráfico', archivo, file_name='Grafico_SP2D.png',
                        mime='image/png')
                if descargar:
                        guardarimagen()
        with col1:
               st.image('./graficoviejo.png', 'última descarga',width=300)                
with tab3:
        """
        #### Autor: Alejandro Rivas \n
        e-mail: elalerivas@gmail.com
        ##### Fecha: 22 de dic de 2022 \n
        Versión: 1.0 \n

        **SimplePlot 2D** es producto del proyecto integrador del curso de la **UTN Santa Fe**, *"Python para docentes"*,
         del programa de postitulación para docentes de la ETP, dictado por el **Prof. Dr. Ariel Loyarte**
        """
        
        
