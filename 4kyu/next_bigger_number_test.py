import next_bigger
import test

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Examples")
    def examples():    
        test.assert_equals(next_bigger(  12),   21)
        test.assert_equals(next_bigger(  21),   -1)
        test.assert_equals(next_bigger( 513),  531)
        test.assert_equals(next_bigger(2017), 2071)
        test.assert_equals(next_bigger( 414),  441)
        test.assert_equals(next_bigger( 144),  414)