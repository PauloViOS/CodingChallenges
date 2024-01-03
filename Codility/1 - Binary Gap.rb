require 'test/unit'

def solution_v2(n)
  longest_gap = 0
  current_gap = 0
  in_gap = false

  n.to_s(2).each_char.with_index do |char, index|
    if char != '0' and in_gap == true
      if current_gap > longest_gap
        longest_gap = current_gap
      end
      in_gap = false
      current_gap = 0

    elsif char != '0'
      current_gap = 0
      in_gap = false
    
    elsif char == '0'
      current_gap += 1
      in_gap = true

    end
  end

  return longest_gap
  
end

class TestLongestGap < Test::Unit::TestCase
  def test_longest_gap
    assert_equal(5, solution_v2(1041))
    assert_equal(0, solution_v2(32))
  end
end

