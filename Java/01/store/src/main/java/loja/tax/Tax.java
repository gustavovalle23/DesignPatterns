package loja.tax;

import java.math.BigDecimal;

import loja.bugdet.Budget;

public interface Tax {

    BigDecimal calculate(Budget budget);

}
