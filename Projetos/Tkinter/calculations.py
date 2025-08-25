
class Calculations:
    """Cálculo de qualidades de polígonos, com base numa lista de coordenadas de pontos que o compõe
    Fonte das fórmulas: https://mv.in.tum.de/_media/members/steger/publications/1996/fgbv-96-05-steger.pdf
    Página 6.
    """

    def __init__(self, List:list, round_value:int = 5, unit:str = None):
        self.List = List
        self.round_value = round_value
        self.unit = unit

    def Is_Counter_Clock_Wise(self):
        try:
            area = 0
            for i in range(0, len(self.List)):
                xi, yi = self.List[i - 1]
                xj, yj = self.List[i]
                area += (xi * yj - xj * yi)
            return area > 0  
        except ZeroDivisionError:
            return 0

    def Moment_of_Inertia_X(self):
        try:
            Ix = 0  
            for i in range(0, len(self.List)):
                xi, yi = self.List[i - 1]
                xj, yj = self.List[i]
                Ix += ((xi * yj - xj * yi) * (yi ** 2 + yi * yj + yj ** 2)) / 12
            return abs(round(Ix, self.round_value))
        except ZeroDivisionError:
            return 0

    def Moment_of_Inertia_Y(self):
        try:
            Iy = 0
            for i in range(0, len(self.List)):
                xi, yi = self.List[i - 1]
                xj, yj = self.List[i]
                Iy += ((xi * yj - xj * yi) * (xi ** 2 + xi * xj + xj ** 2)) / 12
            return abs(round(Iy, self.round_value))
        except ZeroDivisionError:
            return 0

    def Product_of_Inertia(self):
        try:
            Ixy = 0
            for i in range(0, len(self.List)):
                xi, yi = self.List[i - 1]
                xj, yj = self.List[i]
                Ixy += ((xi * yj - xj * yi) * (2 * xi * yi + xi * yj + xj * yi + 2 * xj * yj)) / 24
            
            if not self.Is_Counter_Clock_Wise():
                Ixy *= -1

            return round(Ixy, self.round_value)
        except ZeroDivisionError:
            return 0
    
    def Product_of_Inertia_Centroid(self):
        try:
            Ixy = self.Product_of_Inertia()
            Area = self.Area_of_Polygon()
            dx, dy = self.Centroid_of_polygon_X(), self.Centroid_of_polygon_Y()

            Ixyc = Ixy - Area * dx * dy

            return round(Ixyc, self.round_value)
        except ZeroDivisionError:
            return 0

    def Polar_Moment_of_Inertia(self):
        try:
            Iz = 0
            for i in range(0, len(self.List)):
                xi, yi = self.List[i - 1]
                xj, yj = self.List[i]
                Iz += ((xi * yj - xj * yi) * ((yi ** 2 + yi * yj + yj ** 2) + (xi ** 2 + xi * xj + xj ** 2))) / 12
            return abs(round(Iz, self.round_value))
        except ZeroDivisionError:
            return 0

    def Area_of_Polygon(self):
        try:
            Area = 0
            for i in range(0, len(self.List)):
                xi, yi = self.List[i - 1]
                xj, yj = self.List[i]
                Area += (xi * yj - xj * yi) / 2
            return abs(round(Area, self.round_value))
        except ZeroDivisionError:
            return 0

    def Centroid_of_polygon_X(self):
        try:
            Area = self.Area_of_Polygon()
            xc = 0
            for i in range(0, len(self.List)):
                xi, yi = self.List[i - 1]
                xj, yj = self.List[i]
                xc += ((xi * yj - xj * yi) * (xi + xj)) / (6 * Area)
            return round(xc, self.round_value)
        except ZeroDivisionError:
            return 0

    def Centroid_of_polygon_Y(self):
        try:
            Area = self.Area_of_Polygon()
            yc = 0
            for i in range(0, len(self.List)):
                xi, yi = self.List[i - 1]
                xj, yj = self.List[i]
                yc += ((xi * yj - xj * yi) * (yi + yj)) / (6 * Area)
            return round(yc, self.round_value)
        except ZeroDivisionError:
            return 0

    def Moment_of_Inertia_X_Centroid(self):
        try:
            Ix = self.Moment_of_Inertia_X()
            Area = self.Area_of_Polygon()
            yc = self.Centroid_of_polygon_Y()
            Ixc = Ix - Area * ((yc) ** 2)
            return abs(round(Ixc, self.round_value))
        except ZeroDivisionError:
            return 0

    def Moment_of_Inertia_Y_Centroid(self):
        try:
            Iy = self.Moment_of_Inertia_Y()
            Area = self.Area_of_Polygon()
            xc = self.Centroid_of_polygon_X()
            Iyc = Iy - Area * (xc) ** 2
            return abs(round(Iyc, self.round_value))
        except ZeroDivisionError:
            return 0
        
    def Polar_Moment_of_Inertia_Centroid(self):
        try:
            Ixc = self.Moment_of_Inertia_X_Centroid()
            Iyc = self.Moment_of_Inertia_Y_Centroid()

            return round(Ixc + Iyc, self.round_value)
        except ZeroDivisionError:
            return 0

    def Radius_of_giration_X(self):
        try:
            Kx = (self.Moment_of_Inertia_X()/self.Area_of_Polygon())**.5
            return abs(round(Kx, self.round_value))
        except ZeroDivisionError:
            return 0
    
    def Radius_of_giration_Y(self):
        try:
            Ky = (self.Moment_of_Inertia_Y()/self.Area_of_Polygon())**.5
            return abs(round(Ky, self.round_value))
        except ZeroDivisionError:
            return 0
    
    def Radius_of_giration_X_Centroid(self):
        try:
            Kxc = (self.Moment_of_Inertia_X_Centroid()/self.Area_of_Polygon())**.5
            return abs(round(Kxc, self.round_value))
        except ZeroDivisionError:
            return 0
    
    def Radius_of_giration_Y_Centroid(self):
        try:
            Kyc = (self.Moment_of_Inertia_Y_Centroid()/self.Area_of_Polygon())**.5
            return abs(round(Kyc, self.round_value))
        except ZeroDivisionError:
            return 0

    def Report(self):
    # Dictionary to store results
        results = {
        "Resultados": "",
        "Área": self.Area_of_Polygon(),
        "Centroide": f"{self.Centroid_of_polygon_X()}, {self.Centroid_of_polygon_Y()}",
        "Ix": self.Moment_of_Inertia_X(),
        "Ixc": self.Moment_of_Inertia_X_Centroid(),
        "Iy": self.Moment_of_Inertia_Y(),
        "Iyc": self.Moment_of_Inertia_Y_Centroid(),
        "Ixy": self.Product_of_Inertia(),
        "Ixyc": self.Product_of_Inertia_Centroid(),
        "J": self.Polar_Moment_of_Inertia(),
        "Jc": self.Polar_Moment_of_Inertia_Centroid(),
    }


        report = "Resultados:\n"
        report += "-" * 30 + "\n"
        if not self.unit:
            for key, value in results.items():
                if key == "Resultados":
                    continue  # Skip the placeholder
                report += f"{key}: {value}\n"
        
        else:
            for key, value in results.items():
                if key == "Resultados":
                    continue  # Skip the placeholder
                
                # Add units to relevant keys
                if key in ["Área"]:
                    report += f"{key}: {value} {self.unit}^2\n"
                elif key in ["Ix", "Ixc", "Iy", "Iyc", "Ixy", "Ixyc", "J", "Jc"]:
                    report += f"{key}: {value} {self.unit}^4\n"
                elif key in ["Centroide"]:
                    report += f"{key}: ({value}) {self.unit}\n"
                else:
                    report += f"{key}: {value}\n"

        report += "-" * 30

        return report


    def Values_List(self):
        try:
            return [
                self.Area_of_Polygon(),
                self.Moment_of_Inertia_X(),
                self.Moment_of_Inertia_X_Centroid(),
                self.Moment_of_Inertia_Y(),
                self.Moment_of_Inertia_Y_Centroid(),
                self.Product_of_Inertia(),
                self.Product_of_Inertia_Centroid(),
                self.Polar_Moment_of_Inertia(),
                self.Polar_Moment_of_Inertia_Centroid(),
                (self.Centroid_of_polygon_X(), self.Centroid_of_polygon_Y())
            ]
        except ZeroDivisionError:
            return [0] * 8
