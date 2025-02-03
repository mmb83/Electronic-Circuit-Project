import schemdraw
import schemdraw.elements as elm




def draw_circuit1_PNP_off(d,RB="RB",RC="RC",VCC="VCC"):

    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.Line().length(2.25).left()
    d += elm.Line().length(1.5).up()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(1.4).up()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.SourceV().down().label(VCC)
    d += elm.Line().length(0.7).down()
    d += elm.Line().length(3.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.8).down()
    d += elm.Ground()
    return d
    
def draw_circuit1_PNP_Active(d,RB="RB",RC="RC",VCC="VCC"):
    
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(2.9).up()
    d += elm.Line().length(0.5).right()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Line().length(0.7).right()
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.SourceControlledI().label("ib").reverse()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.SourceV().down().label(VCC)
    d += elm.Line().length(2.5).down()
    d += elm.Line().length(3.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.8).down()
    d += elm.Ground()
    return d

    


def draw_circuit1_PNP_Sat(d,RB="RB",RC="RC",VCC="VCC"):
    
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(2.9).up()
    d += elm.Line().length(0.5).right()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Line().length(0.7).right()
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(0.01).up()
    d += elm.BatteryCell().label("Vce").reverse()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.SourceV().down().label(VCC)
    d += elm.Line().length(2.5).down()
    d += elm.Line().length(3.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.8).down()
    d += elm.Ground()
    return d
    

def draw_circuit1_NPN(d,RB="RB",RC="RC",VCC="VCC"):

    transistor = d.add( elm.BjtNpn(circle=True).label('Q1').right() )
    d += elm.Line().length(2.25).left().at(transistor.base)
    d += elm.Line().length(1.5).up()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Line().length(1.4).up().at(transistor.collector)
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.SourceV().down().reverse().label(VCC)
    d += elm.Line().length(0.7).down()
    d += elm.Line().length(3.5).left()
    
    d += elm.Line().length(1.8).down().at(transistor.emitter)
    d += elm.Ground()
    return d

def draw_circuit1_PNP(d,RB="RB",RC="RC",VCC="VCC"):
    transistor = d.add( elm.BjtPnp2(circle=True).label('Q1').reverse() )
    d += elm.Line().length(2.25).left().at(transistor.base)
    d += elm.Line().length(1.5).up()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Line().length(1.4).up().at(transistor.collector)
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.SourceV().down().reverse().label(VCC).reverse()
    d += elm.Line().length(0.7).down()
    d += elm.Line().length(3.5).left()
    
    d += elm.Line().length(1.8).down().at(transistor.emitter)
    d += elm.Ground()
    return d

def draw_circuit1_NPN_off(d,RB="RB",RC="RC",VCC="VCC"):
    
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.Line().length(2.25).left()
    d += elm.Line().length(1.5).up()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(1.4).up()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.SourceV().down().reverse().label(VCC)
    d += elm.Line().length(0.7).down()
    d += elm.Line().length(3.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.8).down()
    d += elm.Ground()
    return d


    
def draw_circuit1_NPN_Active(d,RB="RB",RC="RC",VCC="VCC"):

    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(2.9).up()
    d += elm.Line().length(0.5).right()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Line().length(0.7).right()
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.SourceControlledI().label("ib").reverse()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.SourceV().down().reverse().label(VCC)
    d += elm.Line().length(2.5).down()
    d += elm.Line().length(3.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.8).down()
    d += elm.Ground()
    return d




def draw_circuit1_NPN_Sat(d,RB="RB",RC="RC",VCC="VCC"):
    
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(2.9).up()
    d += elm.Line().length(0.5).right()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Line().length(0.7).right()
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(0.01).up()
    d += elm.BatteryCell().label("Vce").reverse()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.SourceV().down().reverse().label(VCC)
    d += elm.Line().length(2.5).down()
    d += elm.Line().length(3.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.8).down()
    d += elm.Ground()
    return d

def Analysis_for_circuit1_NPN(RB,Beta,VCC,RC):
    Ibase = (VCC-0.7)/(RB + ((Beta+1) * RC ) )
    if Ibase <= 0 :
        TEMP = "KVL 1: -VCC + (IB + IC) * RC + (IB) * RB + VBE(ACTIVE) = 0"
        return(("off",0,0,VCC),draw_circuit1_NPN_off,TEMP)
    Icollector = Beta * Ibase
    VCE = VCC - ((Beta+1)/Beta) * RC * Icollector 
    if VCE > 0.2 :
        TEMP = "KVL 1: -VCC + (IB + IC) * RC + (IB) * RB + VBE(ACTIVE) = 0 \n KVL 2: -VCC + (BETA+1)/BETA) *RC*IC  + VCE = 0 \n IE = IB + IC"
        return(("Active",Ibase,Icollector,VCE),draw_circuit1_NPN_Active,TEMP)
    else:
        Ibase = (VCC-0.8)/(RB + ((Beta+1) * RC ) )
        Icollector = (VCC - 0.2) / ((Beta+1)/Beta) * RC
        VCE = 0.2
        TEMP = "KVL 1: -VCC + (IB + IC) * RC + (IB) * RB + VBE(SAT) = 0 \n KVL 2: -VCC + (BETA+1)/BETA) *RC*IC  + VCE(SAT) = 0 \n IE = IB + IC"
        return(("Sat",Ibase,Icollector,VCE),TEMP)

def Analysis_for_circuit1_PNP(RB,Beta,VCC,RC):
    Ibase = (VCC-0.7)/(RB + ((Beta+1) * RC ) )
    if Ibase <= 0 :
        TEMP = "KVL 1: VCC - (IB + IC) * RC - (IB) * RB - VEB(ACTIVE) = 0"
        return(("off",0,0,VCC),draw_circuit1_NPN_off,TEMP)
    Icollector = Beta * Ibase
    VEC = VCC - ((Beta+1)/Beta) * RC * Icollector 
    if VCE > 0.2 :
        TEMP = "KVL 1: VCC - (IB + IC) * RC - (IB) * RB - VEB(ACTIVE) = 0 \n KVL 2: VCC - (IB + IC) * RC  - VEC = 0 \n IE = IB + IC"
        return(("Active",Ibase,Icollector,VEC),draw_circuit1_NPN_Active,TEMP)
    else:
        Ibase = (VCC-0.8)/(RB + ((Beta+1) * RC ) )
        Icollector = (VCC - 0.2) / ((Beta+1)/Beta) * RC
        VCE = 0.2
        TEMP = "KVL 1: VCC - (IB + IC) * RC - (IB) * RB - VEB(SAT) = 0 \n KVL 2: VCC - (BETA+1)/BETA) *RC*IC  - VEC(SAT) = 0 \n IE = IB + IC"
        return(("Sat",Ibase,Icollector,VCE),TEMP)


