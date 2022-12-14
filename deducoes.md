a) Segunda lei de newton para a esfera:

$ \vec{R} = \vec{P} + \vec{E} + \vec{D} $

Supondo que a esfera está
afundando no líquido:

$ R\cdot \hat{k} = P \cdot \hat{k} + E \cdot (-\hat{k}) + D \cdot (-\hat{k})  $

$ R = P - E - D $

$ m\dfrac{\partial V}{\partial t} = P - E - \dfrac{1}{2}\rho V^2 AC_D$

b) Mais substituições:

$ E = \rho g \forall$ e  $ P = \rho_s g \forall$

$ \Rightarrow  \rho_s \forall\dfrac{\partial V}{\partial t} = \rho_s g \forall - \rho g \forall - \dfrac{1}{2}\rho V^2 AC_D$

$ \dfrac{\partial V}{\partial t} = \dfrac{(\rho_s - \rho)}{\rho_s} g  - \dfrac{1}{2}\dfrac{\rho}{\rho_s} V^2 \dfrac{\pi R^2}{\frac{4}{3}\pi R^3} C_D $

$ \dfrac{\partial V}{\partial t} = \dfrac{(\rho_s - \rho)}{\rho_s} g  - \dfrac{1}{2}\dfrac{\rho}{\rho_s} V^2 \dfrac{\pi R^2}{\frac{4}{3}\pi R^3} C_D $

$ \dfrac{\partial V}{\partial t} = -g \left(\dfrac{\rho}{\rho_s}  -1 \right)  - \dfrac{3}{4}\dfrac{\rho}{\rho_s}  \dfrac{C_D}{D} V^2$

c) Solução:

Se 
$ \alpha = -g \left(\dfrac{\rho}{\rho_s} - 1 \right) $ 
e 
$ \beta = - \dfrac{3}{4}\dfrac{\rho}{\rho_s}  \dfrac{C_D}{D} $

$ \Rightarrow \dfrac{\partial V}{\partial t} = \alpha + \beta V^2 $

Solução da Equação diferencial:

$ \dfrac{1}{\beta}\dfrac{1}{\frac{\alpha}{\beta} + V^2} \partial V= \partial t $

$ \dfrac{1}{\beta}\int_{V_0}^V\dfrac{1}{\frac{\alpha}{\beta} + V^2} \partial V=\int_0^t \partial t $

$ \dfrac{1}{\beta}\sqrt{\dfrac{\beta}{\alpha}} \text{arctan}\left(V\sqrt{\dfrac{\beta}{\alpha}}\right) - \dfrac{1}{\beta}\sqrt{\dfrac{\beta}{\alpha}} \text{arctan}\left(V_0\sqrt{\dfrac{\beta}{\alpha}}\right)= t $

$ \text{arctan}\left(V\sqrt{\dfrac{\beta}{\alpha}}\right) = \beta\sqrt{\dfrac{\alpha}{\beta}} \cdot t + \text{arctan}\left(V_0\sqrt{\dfrac{\beta}{\alpha}} \right) $

$ V = \sqrt{\dfrac{\alpha}{\beta}}\text{tan}\left(\beta\sqrt{\dfrac{\alpha}{\beta}} \cdot t + \text{arctan}\left(\dfrac{V_0}{\sqrt{\frac{\alpha}{\beta}}} \right) \right)$

d) Derivada do espaço pela velocidade:

$ \dfrac{\partial z}{\partial t} = V$ 
e
$ \dfrac{\partial V}{\partial t} = \alpha + \beta V^2 $

Sabe-se que 
$ \dfrac{\partial z}{\partial t} = \dfrac{\partial z}{\partial V} \cdot \dfrac{\partial V}{\partial t} $

$ \Rightarrow V = \dfrac{\partial z}{\partial V} \cdot (\alpha + \beta V^2) $

$ \Rightarrow \dfrac{\partial z}{\partial V} = \dfrac{V}{\alpha + \beta V^2} $

e) Solução da segunda equação diferencial:

$  \int_0^z\partial z = \dfrac{1}{\beta}\int_{V_0} ^V\dfrac{V}{\frac{\alpha}{\beta} + V^2} \partial V $

$ z = \dfrac{1}{2\beta} ln(\frac{\alpha}{\beta} + V^2) - \dfrac{1}{2\beta} ln(\frac{\alpha}{\beta} + V_0^2) $

$ z = \dfrac{1}{2\beta} ln\left(\dfrac{\frac{\alpha}{\beta} + V^2}{\frac{\alpha}{\beta} + V_0^2}\right) $

f) Profundidade máxima:

$ \dfrac{\partial z}{\partial V} = 0 $

$ \Rightarrow \dfrac{V}{\alpha + \beta V^2} = 0 $

$ \Rightarrow V = 0 $

$ \Rightarrow h = \dfrac{1}{2\beta} ln\left(\dfrac{\frac{\alpha}{\beta}}{\frac{\alpha}{\beta} + V_0^2}\right) $

f2) Tempo de máximo:

Se 
$ V = 0 $
(conforme o ítem anterior)

$ \Rightarrow T = \dfrac{1}{\beta}\sqrt{\dfrac{\beta}{\alpha}} \text{arctan}\left(0\cdot\sqrt{\dfrac{\beta}{\alpha}}\right) - \dfrac{1}{\beta}\sqrt{\dfrac{\beta}{\alpha}} \text{arctan}\left(V_0\sqrt{\dfrac{\beta}{\alpha}}\right) $

$ \Rightarrow T = - \dfrac{1}{\beta\sqrt{\frac{\alpha}{\beta}}} \text{arctan}\left(\dfrac{V_0}{\sqrt{\frac{\alpha}{\beta}}}\right) $


