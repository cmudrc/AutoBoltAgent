import smolagents

class LowFidelityCalculator(transformers.Tool):
    name = "FOS_Calculation"
    description = "Calculates the factor of safety for fasteners using Yield Strength."

    inputs = {
        "desired_safety_factor": {
            "type": "number",
            "description": "Desired factor of safety",
        },
        "load": {
            "type": "number",
            "description": "Load applied to the bolt in Newtons",
        },
        "yield_strength": {
            "type": "number",
            "description": "Yield strength of the bolt material in MPa",
        },
        "preload": {
            "type": "number",
            "description": "Preload applied to the bolt in Newtons",
        },
        "pitch": {
            "type": "number",
            "description": "Pitch of the bolt in mm",
        },
        "E_b": {
            "type": "number",
            "description": "Young's modulus of the bolt in GPa",
        },
        "E_m": {
            "type": "number",
            "description": "Young's modulus of the material in GPa",
        },
        "l": {
            "type": "number",
            "description": "Clamped Length in mm",
        },
        "t_plate": {
            "type": "number",
            "description": "Thickness of the plate in mm",
        },
        "sigma_plate": {
            "type": "number",
            "description": "Yield strength of the plate material in MPa",
        },
        "d_major": {
            "type": "number",
            "description": "Major diameter of the bolt in mm",
        },
        "num_bolts": {
            "type": "number",
            "description": "Number of bolts used in the joint"
        },
    }

    output_type = "number"

    def __init__(self):
        self.ft = ft
        # self.vis = vis

    # def cal_tensile_area(self,d_major,d_minor):
    #     area = (math.pi / 4) * ((d_major + d_minor)/2)**2
    #     return area

    def forward(
            self,
            desired_safety_factor: float,
            d_major: float,
            load: float,
            yield_strength: float,
            preload: float,
            E_b: float,
            E_m: float,
            l: float,
            pitch: float,
            t_plate: float,
            sigma_plate: float,
            num_bolts: int) -> str:

        print(
            f"Inputs: desired_safety_factor={desired_safety_factor}, d_major={d_major}, load={load}, yield_strength={yield_strength}, preload={preload}, pitch={pitch}, \
              E_b={E_b}, E_m={E_m}, l={l}, t_plate={t_plate}, sigma_plate={sigma_plate}, num_bolts={num_bolts}")

        try:
            load_per_bolt = load / num_bolts
            preload_per_bolt = preload / num_bolts
            tensile_area = self.ft.get_tensile_stress_area(d_major, pitch)
            print(f"Calculated Tensile Area: {tensile_area}")
            c = self.ft.get_joint_constant(d_major, l, E_m, E_b)

            bolt_sf = self.ft.bolt_yield_safety_factor(
                c=c, load=load_per_bolt, preload=preload_per_bolt, a_ts=tensile_area, b_ys=yield_strength)

            bearing_Area = d_major * t_plate * num_bolts
            bearing_stress = load / bearing_Area
            allowable_bearing_stress = 1.5 * sigma_plate
            plate_fs = allowable_bearing_stress / bearing_stress
            print(f"Calculated Safety Factor for bolt: {bolt_sf} \n Calculated Safety Factor for plate: {plate_fs}")

            # output = f"Code: Calculate Safety Factor\nResult: {sf:.2f}"
            # print(f"Output: {output}")
            # higher_or_lower = "higher" if sf > desired_safety_factor else "lower"
            # return f"The factor of safety for bolts is {bolt_sf:.2f} and the factor of safety for plates is {plate_fs:.2f}."
            # return sf

            if bolt_sf > desired_safety_factor + 0.1:
                bolt_comparison = "higher than desired"
            elif bolt_sf < desired_safety_factor - 0.1:
                bolt_comparison = "lower than desired"
            else:
                bolt_comparison = "within acceptable range"

            # Compare plate FOS
            if plate_fs > desired_safety_factor + 0.5:
                plate_comparison = "higher than desired"
            elif plate_fs < desired_safety_factor - 0.5:
                plate_comparison = "lower than desired"
            else:
                plate_comparison = "within acceptable range"

            return (
                f"The factor of safety for bolts is {bolt_sf:.2f} ({bolt_comparison}) and "
                f"the factor of safety for plates is {plate_fs:.2f} ({plate_comparison})."
            )

        except requests.RequestException as e:
            error_message = f"Error occurred while fetching data: {str(e)}"
            print(f"Error: {error_message}")
            return f"Action: Error\nResult: {error_message}"
        except KeyError:
            error_message = "Unable to calculate the safety factor. Please check the input values."
            print(f"Error: {error_message}")
            return f"Action: Error\nResult: {error_message}"
        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"
            print(f"Error: {error_message}")
            return f"Action: Error\nResult: {error_message}"
