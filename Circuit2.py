import schemdraw
import schemdraw.elements as elm
from sympy import symbols, Eq, solve


def draw_circuit2_PNP_off(d):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.Resistor().left().label('Rb 200kΩ')
    d += elm.SourceV().down().label('VBB 5V')
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.SourceV().up().reverse().label('Vcc 10V')
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.Line().length(0.5).up()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label('Re 2KΩ')
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_PNP_Active(d):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label('Rb 200kΩ')
    d += elm.SourceV().down().label('VBB 5V')
    d += elm.Line().length(10).right()
    d += elm.Line().length(2.5).up()
    d += elm.SourceV().up().reverse().label('Vcc 10V')
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.SourceControlledI().label("ib").reverse()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label('Re 2KΩ')
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_PNP_Sat(d):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label('Rb 200kΩ')
    d += elm.SourceV().down().label('VBB 5V')
    d += elm.Line().length(10).right()
    d += elm.Line().length(2).up()
    d += elm.SourceV().up().reverse().label('Vcc 10V')
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.BatteryCell().label("vce").reverse()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label('Re 2KΩ')
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_NPN(d):
    d += elm.SourceV().up().label('VBB 5V')
    d += elm.Resistor().right().label('Rb 200kΩ')
    transistor = d.add(elm.BjtNpn(circle=True).label('Q1').right())
    d += elm.Line().length(1).up()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.SourceV().down().reverse().label('Vcc 10V')
    d += elm.Line().length(1.7).down()
    d += elm.Line().length(7.25).left()
    d += elm.Line().length(0).down().at(transistor.emitter)
    d += elm.Resistor().down().label('Re 2KΩ')
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_PNP(d):
    transistor = d.add(elm.BjtPnp2(circle=True).label('Q1').reverse())
    d += elm.Resistor().left().label('Rb 200kΩ').at(transistor.base)
    d += elm.SourceV().down().label('VBB 5V')
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.SourceV().up().reverse().label('Vcc 10V')
    d += elm.Resistor().right().label('3kΩ').at(transistor.collector)
    d += elm.Line().length(0.21).right()
    d += elm.Line().length(1.7).down()
    d += elm.Resistor().down().label('Re 2kΩ').length(0).down().at(transistor.emitter)
    d += elm.Line().length(0.5).down()
    d += elm.Ground()
    return d


def draw_circuit2_NPN_off(d):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.Resistor().left().label('Rb 200kΩ')
    d += elm.SourceV().down().reverse().label('VBB 5V')
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.SourceV().up().label('Vcc 10V')
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.Line().length(0.5).up()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label('Re 2KΩ')
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_NPN_Active(d):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label('Rb 200kΩ')
    d += elm.SourceV().down().reverse().label('VBB 5V')
    d += elm.Line().length(10).right()
    d += elm.Line().length(2.5).up()
    d += elm.SourceV().up().label('Vcc 10V')
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.SourceControlledI().label("ib").reverse()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label('Re 2KΩ')
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_NPN_Sat(d):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label('Rb 200kΩ')
    d += elm.SourceV().down().reverse().label('VBB 5V')
    d += elm.Line().length(10).right()
    d += elm.Line().length(2).up()
    d += elm.SourceV().up().label('Vcc 10V')
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.BatteryCell().label("vce").reverse()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label('Re 2KΩ')
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def Analysis_for_circuit2_NPN(VBB, RB, RE, Beta, VCC, RC):
    Ibase = (VBB-0.7)/(RB + RE*(Beta+1))
    if Ibase <= 0:
        return ("off")
    Icollector = Beta * Ibase
    VCE = VCC - Icollector * (RC + ((Beta+1)/Beta)*RE)
    if VCE > 0.2:
        return (("Active", Ibase, Icollector, VCE))
    else:
        Ibase, Icollector = symbols('Ibase,Icollector')
        eq1 = Eq(Ibase*(RB + RE) + Icollector*RE, VBB-0.8)
        eq2 = Eq(Ibase*RB + Icollector*(RC + RE), VCC-0.2)
        sol = solve((eq1, eq2), (Ibase, Icollector))
        return (("Sat", sol[Ibase], sol[Icollector], 0.2))


def Analysis_for_circuit2_PNP(VBB, RB, RE, Beta, VCC, RC):
    Ibase = (0.7 - VBB) / (RB + RE * (Beta + 1))
    if Ibase >= 0:  
        return ("off")
    Icollector = Beta * Ibase
    VCE = VCC - Icollector * (RC + ((Beta + 1) / Beta) * RE)
    
    if VCE > 0.2:
        return ("Active", Ibase, Icollector, VCE)
    else:
        Ibase, Icollector = symbols('Ibase Icollector')
        eq1 = Eq(Ibase * (RB + RE) + Icollector * RE, 0.7 - VBB)
        eq2 = Eq(Ibase * RB + Icollector * (RC + RE), VCC - 0.2)
        sol = solve((eq1, eq2), (Ibase, Icollector))
        return ("Sat", sol[Ibase], sol[Icollector], 0.2)

