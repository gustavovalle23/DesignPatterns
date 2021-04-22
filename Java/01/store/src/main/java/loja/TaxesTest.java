package loja;

import java.math.BigDecimal;

import loja.tax.TaxesCalculator;
import loja.bugdet.Budget;
import loja.tax.ICMS;
import loja.tax.ISS;

public class TaxesTest {
    public static void main(String[] args) {
        Budget orcamento = new Budget(new BigDecimal("100"));
        TaxesCalculator calculadora = new TaxesCalculator();

        System.out.println(calculadora.calculate(orcamento, new ISS()));
        System.out.println(calculadora.calculate(orcamento, new ICMS()));

    }
}
