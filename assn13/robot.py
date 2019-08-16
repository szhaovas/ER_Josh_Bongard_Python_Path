import constants as c


class ROBOT:
    def __init__(self, sim, wts):

        O0 = sim.send_box(
            x=0,
            y=0,
            z=c.L + c.R,
            length=c.L,
            width=c.L,
            height=2 * c.R,
            r=0.5,
            g=0.5,
            b=0.5)
        O1 = sim.send_cylinder(
            x=c.L,
            y=0,
            z=c.L + c.R,
            length=c.L,
            radius=c.R,
            r1=1,
            r2=0,
            r3=0,
            r=0,
            g=1,
            b=0)
        O2 = sim.send_cylinder(
            x=0,
            y=c.L,
            z=c.L + c.R,
            length=c.L,
            radius=c.R,
            r1=0,
            r2=1,
            r3=0,
            r=1,
            g=0,
            b=0)
        O3 = sim.send_cylinder(
            x=-c.L,
            y=0,
            z=c.L + c.R,
            length=c.L,
            radius=c.R,
            r1=1,
            r2=0,
            r3=0,
            r=0.5,
            g=0,
            b=0.5)
        O4 = sim.send_cylinder(
            x=0,
            y=-c.L,
            z=c.L + c.R,
            length=c.L,
            radius=c.R,
            r1=0,
            r2=1,
            r3=0,
            r=0,
            g=0,
            b=1)

        O5 = sim.send_cylinder(x=c.L * 3 / 2,
                               y=0,
                               z=(c.L + c.R) / 2,
                               length=c.L,
                               radius=c.R,
                               r1=0,
                               r2=0,
                               r3=1,
                               r=0,
                               g=1,
                               b=0)
        O6 = sim.send_cylinder(x=0,
                               y=c.L * 3 / 2,
                               z=(c.L + c.R) / 2,
                               length=c.L,
                               radius=c.R,
                               r1=0,
                               r2=0,
                               r3=1,
                               r=1,
                               g=0,
                               b=0)
        O7 = sim.send_cylinder(x=-c.L * 3 / 2,
                               y=0,
                               z=(c.L + c.R) / 2,
                               length=c.L,
                               radius=c.R,
                               r1=0,
                               r2=0,
                               r3=1,
                               r=0.5,
                               g=0,
                               b=0.5)
        O8 = sim.send_cylinder(x=0,
                               y=-c.L * 3 / 2,
                               z=(c.L + c.R) / 2,
                               length=c.L,
                               radius=c.R,
                               r1=0,
                               r2=0,
                               r3=1,
                               r=0,
                               g=0,
                               b=1)

        J0 = sim.send_hinge_joint(
            first_body_id=O0,
            second_body_id=O1,
            x=c.L / 2,
            y=0,
            z=c.L + c.R,
            n1=0,
            n2=1,
            n3=0)
        J1 = sim.send_hinge_joint(
            first_body_id=O0,
            second_body_id=O2,
            x=0,
            y=c.L / 2,
            z=c.L + c.R,
            n1=1,
            n2=0,
            n3=0)
        J2 = sim.send_hinge_joint(
            first_body_id=O0,
            second_body_id=O3,
            x=-c.L / 2,
            y=0,
            z=c.L + c.R,
            n1=0,
            n2=1,
            n3=0)
        J3 = sim.send_hinge_joint(
            first_body_id=O0,
            second_body_id=O4,
            x=0,
            y=-c.L / 2,
            z=c.L + c.R,
            n1=1,
            n2=0,
            n3=0)

        J4 = sim.send_hinge_joint(
            first_body_id=O1,
            second_body_id=O5,
            x=c.L * 3 / 2,
            y=0,
            z=c.L + c.R,
            n1=0,
            n2=1,
            n3=0)
        J5 = sim.send_hinge_joint(
            first_body_id=O2,
            second_body_id=O6,
            x=0,
            y=c.L * 3 / 2,
            z=c.L + c.R,
            n1=1,
            n2=0,
            n3=0)
        J6 = sim.send_hinge_joint(
            first_body_id=O3,
            second_body_id=O7,
            x=-c.L * 3 / 2,
            y=0,
            z=c.L + c.R,
            n1=0,
            n2=1,
            n3=0)
        J7 = sim.send_hinge_joint(
            first_body_id=O4,
            second_body_id=O8,
            x=0,
            y=-c.L * 3 / 2,
            z=c.L + c.R,
            n1=0,
            n2=1,
            n3=0)

        T0 = sim.send_touch_sensor(body_id=O5)
        T1 = sim.send_touch_sensor(body_id=O6)
        T2 = sim.send_touch_sensor(body_id=O7)
        T3 = sim.send_touch_sensor(body_id=O8)
        # self.P4 = sim.send_position_sensor(body_id=O0)
        self.L5 = sim.send_light_sensor(body_id=O0)

        SN0 = sim.send_sensor_neuron(sensor_id=T0)
        SN1 = sim.send_sensor_neuron(sensor_id=T1)
        SN2 = sim.send_sensor_neuron(sensor_id=T2)
        SN3 = sim.send_sensor_neuron(sensor_id=T3)
        SN4 = sim.send_sensor_neuron(sensor_id=self.L5)
        SN = {0: SN0, 1: SN1, 2: SN2, 3: SN3, 4: SN4}
        MN4 = sim.send_motor_neuron(joint_id=J0, tau=0.3)
        MN5 = sim.send_motor_neuron(joint_id=J1, tau=0.3)
        MN6 = sim.send_motor_neuron(joint_id=J2, tau=0.3)
        MN7 = sim.send_motor_neuron(joint_id=J3, tau=0.3)
        MN8 = sim.send_motor_neuron(joint_id=J4, tau=0.3)
        MN9 = sim.send_motor_neuron(joint_id=J5, tau=0.3)
        MN10 = sim.send_motor_neuron(joint_id=J6, tau=0.3)
        MN11 = sim.send_motor_neuron(joint_id=J7, tau=0.3)
        MN = {0: MN4, 1: MN5, 2: MN6, 3: MN7, 4: MN8, 5: MN9, 6: MN10, 7: MN11}

        for sn in SN:
            for mn in MN:
                sim.send_synapse(
                    source_neuron_id=SN[sn], target_neuron_id=MN[mn], weight=wts[sn, mn])
        # whiteObject = sim.send_cylinder(z=0.6, length=1.0, radius=0.1)
        # redObject = sim.send_cylinder(
        #     y=0.5, z=1.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)
        # joint = sim.send_hinge_joint(
        #     first_body_id=whiteObject,
        #     second_body_id=redObject,
        #     z=1.1,
        #     n1=-1,
        #     lo=-3.14159 / 2,
        #     hi=3.14159 / 2)

        # T0 = sim.send_touch_sensor(body_id=whiteObject)
        # T1 = sim.send_touch_sensor(body_id=redObject)
        # P2 = sim.send_proprioceptive_sensor(joint_id=joint)
        # R3 = sim.send_ray_sensor(
        #     body_id=redObject,
        #     x=0,
        #     y=0.55,
        #     z=1.1,
        #     r1=0,
        #     r2=0,
        #     r3=-1)
        # self.P4 = sim.send_position_sensor(body_id=whiteObject)
        #
        # SN0 = sim.send_sensor_neuron(sensor_id=T0)
        # SN1 = sim.send_sensor_neuron(sensor_id=T1)
        # SN2 = sim.send_sensor_neuron(sensor_id=P2)
        # SN3 = sim.send_sensor_neuron(sensor_id=R3)
        # sensorNeurons = {}
        # sensorNeurons[0] = SN0
        # sensorNeurons[1] = SN1
        # sensorNeurons[2] = SN2
        # sensorNeurons[3] = SN3
        #
        # MN4 = sim.send_motor_neuron(joint_id=joint)
        # motorNeurons = {}
        # motorNeurons[0] = MN4
        #
        # for s in sensorNeurons:
        #     for m in motorNeurons:
        #         sim.send_synapse(
        #             source_neuron_id=sensorNeurons[s],
        #             target_neuron_id=motorNeurons[m],
        #             weight=wts[s])
