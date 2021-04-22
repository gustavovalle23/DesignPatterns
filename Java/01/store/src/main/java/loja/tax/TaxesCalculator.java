package loja.tax;

import java.math.BigDecimal;

import loja.bugdet.Budget;

public class TaxesCalculator {

    public BigDecimal calculate(Budget budget, Tax tax) {
        return tax.calculate(budget);
    }

}
