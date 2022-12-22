import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #importo para trabajar con tablas
from sympy import *
x, y, z, t = symbols('x y z t')
#import time
#import re



tab1, tab2, tab3 = st.tabs(['Ley de Ohm','Gráficos','Funciones'])
with tab1:

    """
    # Ley de Ohm
    $ I = \cfrac {V}{R} $
    * $ I $ : Corriente eléctrica
    * $ V $: Tensión aplicada
    * $ R $: Resistencia eléctrica (en $ \Omega$).
    $ A = \int_{2}^{3} \\theta \\times dt = \\begin{pmatrix}
    2 & 3 \\\\
    5 & 8  \\\\
    \end{pmatrix} $

    """
    boton = st.button('Hacer click')
    if boton is True:
         st.write('Boton presionado')

    numero= st.number_input('seleccionar valor',min_value=1,max_value=5,value=2)
    st.write(f'El numero seleccionado es {numero}')
with st.sidebar:
    """
    # Amplitudes
    """
    armonicos = [1, 2, 3, 4, 5, 6, 7]
    Hrmy = st.selectbox('Armónico',armonicos)
    st.write(f'Armónicos 1 y {Hrmy}')
    A = st.slider('Amplitud A',min_value=0,max_value=100,value=1,step=10)
    
    B = st.slider('Amplitud B',min_value=0,max_value=100,value=1,step=10)
    st.write(f'Amplitud del armónico 1 = {A/(A+B)*100:.1f}%')
    st.write(f'Amplitud del armónico {Hrmy} = {B/(A+B)*100:.1f}%')
    phi= st.slider('Desfasaje',min_value=0,max_value=180,value=1,step=1)

with tab2:  
    xx=np.linspace(0,3*np.pi,300)
    phi = phi * np.pi/180
    y= A*np.sin(xx)+B*np.sin(Hrmy*xx + phi)
    #objeto=np.array([x],[y])
    #print(objeto)
    f=plt.figure(figsize=(9,3))
    #plt.plot('x','y',data=objeto)
    graf=plt.plot(xx,y,'gx-',lw=2,markersize=4,mec='b', label='superposicion')
    plt.legend() # para que se muestre los labels
    plt.xlabel('tiempo')
    plt.ylabel('amplitud')
    plt.axis([0,10,-100,100])
    plt.suptitle('Superposición de armónicos')
    # 'g' == color='g', 'x' == marker='x', '--' == ls='dashed'
    """
    $ f(x) =\\frac{sin(x)}{x^{2}}$
    """
    f
    with tab3:
        
        col1, col2, col3 = st.columns(3)
        #codCol=['b','g','r','c','m','y','k','w']
        
        #dicColores ={'colores':colores, 'codigo':codCol}
        
        with col1:
            x0=st.number_input('xmin',value=-10.0, step=0.1)
            xf=st.number_input('xmax',value=10.0, step=0.1)
            resol=st.number_input('resolución',min_value=10, max_value=400,value=300, step=10)
        with col2:
            colores=['azul', 'verde', 'rojo', 'cian', 'magenta', 'amarillo', 'negro', 'blanco']
            color=st.selectbox('color linea',colores,index=0)
            dicColor={'rojo':'r','azul':'b','verde':'g','cian':'c','magenta':'m','amarillo':'y','negro':'k','blanco':'w'}
            color=dicColor[color]

            marcas=['ninguna','punto', 'circulo', 'triangulo', 'cuadrado', 'estrella', 'exagono', 'cruz1', 'cruz2']
            marca=st.selectbox('tipo de marca',marcas,index=0)
            dicMarca={'ninguna':'','punto':'.', 'circulo':'o', 'triangulo':'^', 'cuadrado':'s', 'estrella':'*', 'exagono':'H', 'cruz1':'x', 'cruz2':'+'}
            marca=dicMarca[marca]
            
            estilos=['ninguna','solido', 'trazos', 'rayapunto', 'dospuntos', 'punteada']
            estilo=st.selectbox('tipo de linea',estilos,index=1)
            dicEstilo={'ninguna':'','solido':'-', 'trazos':'--', 'rayapunto':'-.', 'dospuntos':':', 'punteada':'dotted'}
            estilo=dicEstilo[estilo]
        with col3:
           
            ancholin=st.number_input('ancho linea',min_value=1, max_value=8,value=2,step=1)
            
            colores=['azul', 'verde', 'rojo', 'cian', 'magenta', 'amarillo', 'negro', 'blanco']
            colorMark=st.selectbox('color marca',colores,index=0)
            dicColor={'rojo':'r','azul':'b','verde':'g','cian':'c','magenta':'m','amarillo':'y','negro':'k','blanco':'w'}
            colorMark=dicColor[colorMark]
            
            SizeMarca=st.number_input('tamaño marca',min_value=1, max_value=8,value=2,step=1)
            
        #subplot 1

        func_orig=['pow','PI','sqrt','exp','ln','log','sin','cos','tan','asin','acos','atan','hsin','hcos','htan','abs']
        reemplazo=['np.power','np.pi','np.sqrt','np.exp','np.log','np.log10','np.sin','np.cos','np.tan','np.asin',      
                                                                'np.acos','np.atan','np.sinh','np.cosh','np.tanh','np.absolute']

        funcion=st.text_input('Ingrese Funcion',placeholder='f(x) = exp(-pow(x,2))*sin(5*x)')    
        parentesis=[funcion.count('('),funcion.count(')')]
        if parentesis[0] > parentesis[1]:
            st.write('Revisar paréntesis. Falta " ) "')
        if parentesis[0] < parentesis[1]:
            st.write('Revisar paréntesis. Falta " ( "')

            
        
        if funcion == '':
            funcion = 'exp(-pow(x,2))*sin(5*x)'

        #exec(f'funcion0={funcion}')
        st.write(funcion)
        st.latex(funcion)
        st.latex(latex(funcion))
        st.latex('f(x)='+latex(pow(x,2) ))
        st.write(latex(funcion))
        prueba=latex(funcion)
        prueba
        for i in range (0,len(func_orig)):

          
            funcion=funcion.replace(func_orig[i],reemplazo[i])

           # with st.spinner('convirtiendo a numpy...'):
           #     time.sleep(0.1)
           #     st.success('Listo!')
        
        

        x=np.linspace(x0,xf,resol)
        #x=np.linspace(-1,4,300)
        phi = phi * np.pi/180

              
        
        exec(f'funcion={funcion}')
        
        
        y=funcion
        
       # puntos={'x':x,'y':y}
        #tabla=pd.DataFrame(data=puntos)

        print(x)
        #y= A*np.sin(x)+B*np.sin(Hrmy*x + phi)
        
        #hImagen=st.slider('ancho imagen',min_value=3, max_value=10,value=8,step=1)
        vImagen=st.slider('alto imagen',min_value=3, max_value=10,value=4,step=1)

        ff=plt.figure(figsize=(9,vImagen),facecolor=colorMark)
        plt.grid(which='both', fillstyle='right')
        #ff.add_axes([0.1,0.5,0.5,0.5])
        #ax1=plt.subplot(331) 
        leyenda = 'Superposición'

        graf=plt.plot(x,y,c=color,ls= estilo ,marker=marca,lw=ancholin,markersize=SizeMarca,mec=colorMark, label= leyenda)
        #plt.text(5, 0.5, r'$\mu=100,\ \sigma=15$')
        plt.legend() # para que se muestre los labels
        plt.xlabel('x')
        plt.ylabel('f(x)')
        #plt.axis([x0,xf,-100,100])
        plt.suptitle('Superposición de armónicos')
        
        #ax3=plt.subplot(333,sharex=ax1)
        #plt.plot(x,y,c=color,ls= estilo ,marker=marca,lw=ancholin,markersize=SizeMarca,mec=colorMark, label= leyenda)
        
        ff

        #    pruebas   
        
    #    agree = st.checkbox('Mostrar ejes')
    #    if agree:   
    #            st.write('Great!')
    #    genre = st.radio("What's your favorite movie genre",
    #                   ('Comedy', 'Drama', 'Documentary'))

    #    if genre == 'Comedy':
    #        st.write('You selected comedy.')
    #    else:
    #        st.write("You didn't select comedy.")
    #    options = st.multiselect('What are your favorite colors',
    #                              ['Green', 'Yellow', 'Red', 'Blue'],
     #                                ['Yellow', 'Red'])

     #   st.write('You selected:', options)
     #   color = st.color_picker('Pick A Color', '#00f900')
     #   st.write('The current color is', color)
    #    import streamlit as st
       
        
    #    picture = st.camera_input("Take a picture")

    #    if picture:
    #        st.image(picture) 
    
        