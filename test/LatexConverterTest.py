import unittest
from src.LatexConverter import LatexConverter

class LatexConverterTest(unittest.TestCase):

    def setUp(self):
        self.sut = LatexConverter()

    def testExtractBoundingBox(self):
        pass
    
    def testCorrectBoundingBoxAspectRaito(self):
        pass

    def testConvertExpressionToPng(self):
        binaryData = self.sut.convertExpressionToPng("$x^2$", 115).read()
        with open('resources/test/xsquared.png', "rb") as f:
            correctBinaryData = f.read()
        self.assertAlmostEqual(len(binaryData),len(correctBinaryData), delta=5)
        
        binaryData = self.sut.convertExpressionToPng("$x^2$"*10, 115).read()
        with open('resources/test/xsquared10times.png', "rb") as f:
            correctBinaryData = f.read()
        self.assertAlmostEqual(len(binaryData),len(correctBinaryData), delta=5)
        
        self.sut.setPreambleId("11")
        binaryData = self.sut.convertExpressionToPng("$x^2$"*10, 115).read()
        
if __name__ == '__main__':
    unittest.main()
    
